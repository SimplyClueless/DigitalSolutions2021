from deviceFunctions import Database, GPIODevices, Email, Camera
import RPi.GPIO as GPIO
import time

def startup():
    global led
    global accelerometer
    global tempSensor
    global heartSensor
    global emergencyToggle
    global db

    # Sets device LED to green on startup
    led = GPIODevices.RGBLed()
    led.SetColor(False, True, False)
    accelerometer = GPIODevices.Accelerometer() 
    tempSensor = GPIODevices.TempSensor()
    heartSensor = GPIODevices.HeartSensor()
    db = Database("35.201.1.208", "root", "Sheldon#1", "benHealthService") 
    emergencyToggle = False

    while True:
        readVitals()

def getSerial():
    cpuserial = "0000000000000000" # Gets the device serial number for later use
    try:
        file = open('/proc/cpuinfo', 'r') # File where serial number is stored
        for line in file:
            if line[0:6]=="Serial": # Checks if the serial number is in the file
                cpuserial = line[10:26] # Saves the serial number from the file
        file.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial # Returns value to where function is called

def readVitals():
    global emergencyToggle
    global db

    # Gets all the returned values and stores them locally
    deviceID = getSerial()
    heartVal = heartSensor.ReturnValue(1)
    accel = accelerometer.ReturnValue()
    tempVal = tempSensor.ReturnValue(0)

    # Adds the collected data to the database
    query = "INSERT INTO deviceInformation (deviceID, heartRate, acceleration, temperature) VALUES (%s, %s, %s, %s)"
    values = (deviceID, heartVal, accel, tempVal)
    db.ImportData(query, values)
    db.Commit()

    # Fall detection with accelerometer value
    if emergencyToggle == False:
        if (accel >= 2.5): alert()

def alert(): # Code for button to cancel fall warning
    led.Off() # Turns of LED
    toggle = False
    print("Starting Warning Shutoff Timer")
    
    cycle = 30 # Sets number of seconds to run loop for
    while cycle >= 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        inputValue = GPIO.input(26)

        if toggle == False: # Flash LED red
            led.SetColor(True, False, False)
            toggle = True

        elif toggle == True: # Turn off LED
            led.Off()
            toggle = False

        # Checks if button is pressed
        if (inputValue == False): 
            print("Button Pressed")
            break # Breaks from loop
        
        print(f'Time remaining: {cycle/2}')
        print(f'Cycle: {cycle}')
        cycle -= 1
        time.sleep(0.5)
    
    # If the cycle is finished trigger alert
    if not (cycle >= 0):
        emergencyNotification()
        # Sets LED to red
        led.SetColor(True, False, False) 
    else:
        led.Off() # Turns off LED
        print("Warning Timer Stopped")

def emergencyNotification():
    global emergencyToggle
    global db

    # Stops the loop in data collection function
    emergencyToggle = True
    print("Sending information to emergency services...")
   
    deviceID = getSerial() # Saves CPU serial number
    # Gets the patients details to correctly send the email
    query = "SELECT * FROM patientData WHERE deviceID = '%s'" % (deviceID)
    records = db.ReturnData(query)
    # Save patients first name, last name and email address
    for row in records:
        firstName = row[3]
        lastName = row[4]
        emailAddress = row[5]
    
    camera = Camera() # Defines the Camera from class
    camera.Record(15) # Sets the camera to record for 15 seconds

    # Connects to the email server using the server account details, address to send to and email subject
    email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", emailAddress, "Emergency Alert Notification")
    # Attaches a standard message with the patients name returned from the databse
    email.AttachText(f"An emergency alert has been triggered on a device attached to this email address\n\nFirst Name - {firstName}\nLast Name - {lastName}")
    # Attaches the video recorded from the device camera
    email.AttachFile("cameraCapture.mp4")
    email.SendEmail()

# Runs function on start if this is the main application
if __name__ == '__main__':
    startup()
