from deviceFunctions import Database, Accelerometer, GPIODevices, Email, Camera
import RPi.GPIO as GPIO
import time

#db.ShowTables()
#db.ShowVariables("customers")

#query = "SELECT * FROM customers"
#db.ReturnData(query)

#db.Commit()
#db.Close()

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
    accelerometer = Accelerometer() 
    tempSensor = GPIODevices.TempSensor()
    heartSensor = GPIODevices.HeartSensor()
    db = Database("35.201.1.208", "root", "Sheldon#1", "benHealthService") 
    emergencyToggle = False

    while True:
        readVitals()

def getSerial():
    cpuserial = "0000000000000000"
    try:
        file = open('/proc/cpuinfo', 'r')
        for line in file:
            if line[0:6]=="Serial":
                cpuserial = line[10:26]
        file.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial

def readVitals():
    global emergencyToggle
    global db

    deviceID = getSerial()
    heartVal = heartSensor.ReturnValue(1)
    accel = accelerometer.ReturnValue()
    tempVal = tempSensor.ReturnValue(0)

    query = "INSERT INTO deviceInformation (deviceID, heartRate, acceleration, temperature) VALUES (%s, %s, %s, %s)"
    values = (deviceID, heartVal, accel, tempVal)
    db.ImportData(query, values)
    db.Commit()

    if emergencyToggle == False:
        if (
                (accel >= 2.5)
                ):
            alert()

    #if emergencyToggle == False:
    #    if (
    #            (accel >= 2.5) or 
    #            (tempVal <= 340) or (tempVal >= 390) or 
    #            (heartVal <= 50) or (heartVal >= 90)
    #            ):
    #        alert()

# Code for button to cancle fall warning
def alert(): 
    led.Off()
    toggle = False
    print("Starting Warning Shutoff Timer")
    
    cycle = 20
    while cycle >= 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        inputValue = GPIO.input(26)

        if toggle == False: 
            led.SetColor(True, False, False)
            toggle = True

        elif toggle == True: 
            led.Off()
            toggle = False

        if (inputValue == False):
            print("Button Pressed")
            break
        
        print(f'Time remaining: {cycle/2}')
        print(f'Cycle: {cycle}')
        cycle -= 1
        time.sleep(0.5)
    
    if not (cycle >= 0):
        emergencyNotification()
        led.SetColor(True, False, False)
    else:
        led.Off()
        print("Warning Timer Stopped")

def emergencyNotification():
    global emergencyToggle
    global db

    emergencyToggle = True
    print("Sending information to emergency services...")
   
    deviceID = getSerial()
    query = "SELECT * FROM patientData WHERE deviceID = '%s'" % (deviceID)
    records = db.ReturnData(query)
    for row in records:
        firstName = row[3]
        lastName = row[4]
        emailAddress = row[5]
    
    camera = Camera()
    camera.Record(15)

    email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", emailAddress, "Emergency Alert Notification")
    email.AttachText(f"An emergency alert has been triggered on a device attached to this email address\n\nFirst Name - {firstName}\nLast Name - {lastName}")
    email.AttachFile("cameraCapture.mp4")
    email.SendEmail()

if __name__ == '__main__':
    startup()
