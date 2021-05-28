# Database Module
import mysql.connector

# Email Modules
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Camera Modules
import cv2
import numpy as np
from datetime import datetime

# Accelerometer Modules
import msa301
import math

# GPIO Modules
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Other Modules
import time

class Database:
    def __init__(self, host, user, password, database): # Creates SQL databse connection using account details passed on class creation
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.connection.cursor(buffered=True) # Creates SQL cursor for query execution

    def ShowTables(self): # Prints all the tables in the connected database
        self.cursor.execute("SHOW TABLES") # Searches for all tables in the database file
        result = self.cursor.fetchall() # Gets all values returned
        for table in result:
            print(table) # Prints values to console

    def ShowVariables(self, table): # Print all variables from the defined table
        self.cursor.execute(f"SELECT * FROM {table}")
        columns = [tuple[0] for tuple in self.cursor.description] # Orders the variables in readable view
        print(columns)

    # SELECT "" FROM ""
    def ReturnData(self, query):
        self.cursor.execute(query)

        result = self.cursor.fetchall() # Gets all values returned
        for value in result: 
            print(value) # Prints values to console

        return result # Returns all values to where the function was called

    def DeleteAllData(self, table): # Deletes all data from a specified table passed on function call
        self.cursor.execute(f"DELETE FROM {table}")

    def ImportData(self, query, values): # Custom cursor execute INSERT using class 'self.' variables
        self.cursor.execute(query, values)

    def Commit(self): # Custom commit using class 'self.' variables
        self.connection.commit()

    def Close(self): # Custom close using class 'self.' variables
        self.connection.close()

class Email:
    def __init__(self, email, password, sendToEmail, subject): # Sets up basic Email details passed in class creation
        self.email = email # Send from email
        self.password = password # Send from email password
        self.sendToEmail = sendToEmail # Sends email to this address
        self.subject = subject # Email subject

        self.msg = MIMEMultipart() # Sets up the email template
        self.msg["Subject"] = self.subject
        self.msg["From"] = self.email
        self.msg["To"] = self.sendToEmail

    def SendEmail(self): # Sends the Email using the set variables
        context = ssl.create_default_context()
        self.message = self.msg.as_string()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.email, self.password) # Uses details to connect to sending email account
            server.sendmail(self.email, self.sendToEmail, self.message) # Sends email using email addresses and formed message
            server.quit()

        print("Email Sent!")

    def AttachText(self, text): # Atteches a string variable to the Email
        self.msg.attach(MIMEText(text, "plain"))

    def AttachFile(self, file): # Attaches a specified file to the Email
        filename = file
        with open(filename, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read()) # Reads the file from the system
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        self.msg.attach(part)

class Camera:
    def __init__(self): # Set up basic OpenCV2 variables
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 24) # Sets video framerate
        self.cam.set(3, 1280) # Sets video width
        self.cam.set(4, 720) # Sets video height

        self.font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter("cameraCapture.mp4", self.fourcc, 24, (1280, 720))

    # Starts recording from the camera based on a certain time passed when the functions is called
    def Record(self, recordTime):
        tick = 0 # Local cycle variable

        while tick < recordTime * 100: # Adds a buffer to the local cycle and record time
            self.ret, self.img = self.cam.read()
            self.img = cv2.flip(self.img, 0)
            tick += 1

        self.cam.release()
        cv2.destroyAllWindows()

class GPIODevices:
    class Accelerometer:
        def __init__(self): # Sets up accelerometer sensor using specified module
            self.accel = msa301.MSA301()
            self.accel.reset()
            self.accel.set_power_mode('normal')

        def ReturnValue(self): # Gets the acceleration values and performs calculation to get overall magnitude
            firstx, firsty, firstz = self.accel.get_measurements()
            time.sleep(0.5) 
            lastx, lasty, lastz = self.accel.get_measurements()

            finalx = firstx - lastx # Finds the difference between the first and last variable to find the movement along axis
            finaly = firsty - lasty # Finds the difference between the first and last variable to find the movement along axis
            finalz = firstz - lastz # Finds the difference between the first and last variable to find the movement along axis

            magnitude = math.sqrt(finalx * finalx + finaly * finaly + finalz * finalz) # Uses pythagoras to find one overall magnitude of the 3 axis

            print(f'Movement magnitude: {magnitude}')
            return magnitude # Returns the magnitude to where the function was called

    class RGBLed:
        def __init__(self):
            self.pins = {'redPin':21, 'greenPin':20, 'bluePin':16} # Sets the pins for each LED colour

        def SetColor(self, red, green, blue): # Turns on the LED based on what colours are active
            GPIO.setmode(GPIO.BCM)

            if red == True: # Turns on red LED
                GPIO.setup(self.pins['redPin'], GPIO.OUT)
                GPIO.output(self.pins['redPin'], GPIO.HIGH)

            if green == True: # Turns on green LED
                GPIO.setup(self.pins['greenPin'], GPIO.OUT)
                GPIO.output(self.pins['greenPin'], GPIO.HIGH)

            if blue == True: # Turns on blue LED
                GPIO.setup(self.pins['bluePin'], GPIO.OUT)
                GPIO.output(self.pins['bluePin'], GPIO.HIGH)

        def Off(self): # Turns off all LED colours
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pins['redPin'], GPIO.OUT)
            GPIO.output(self.pins['redPin'], GPIO.LOW)
            GPIO.setup(self.pins['greenPin'], GPIO.OUT)
            GPIO.output(self.pins['greenPin'], GPIO.LOW)
            GPIO.setup(self.pins['bluePin'], GPIO.OUT)
            GPIO.output(self.pins['bluePin'], GPIO.LOW)
            GPIO.cleanup()

    class TempSensor:
        def __init__(self): # Sets up the sensor with the Digital to Analog converter
            self.SPI_PORT = 0 # Sets hardware ports
            self.SPI_DEV = 0
            self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEV))

        def ReturnValue(self, analogPort):
            # Reads value from converter port
            raw = self.mcp.read_adc(analogPort)
            # Multiplies 1023 value by the voltage to find actual temp
            temp = ((raw * 330)/float(1023))-50
            # Rounds temp to 2 decimal places
            temp = round(temp, 2)

            print(f'Temperature: {temp}')
            # Returns value to where the function is called
            return temp

    class HeartSensor:
        def __init__(self): # Sets up the sensor with the Digital to Analog converter
            self.SPI_PORT = 0 # Sets hardware ports
            self.SPI_DEV = 0
            self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEV))

        def ReturnValue(self, analogPort):
            rate = self.mcp.read_adc(analogPort) # Reads value from converter port

            print(f'Heart Rate: {rate}')
            return rate # Returns value to where the function is called
