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
    # Creates SQL Database connection using account details passed into class creation
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.connection.cursor(buffered=True)

    # Prints all the tables in the connected database
    def ShowTables(self):
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        for table in result:
            print(table)

    # Print all the variables in the defined table
    def ShowVariables(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        columns = [tuple[0] for tuple in self.cursor.description]
        print(columns)

    # SELECT "" FROM ""
    def ReturnData(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for value in result:
            print(value)

        return result
    def DeleteAllData(self, table):
        self.cursor.execute(f"DELETE FROM {table}")

    # INSERT INTO "" (var, var) VALUES (%s, %s)
    def ImportData(self, query, values):
        self.cursor.execute(query, values)

    def Commit(self):
        self.connection.commit()

    def Close(self):
        self.connection.close()

class Email:
    # Sets up basic Email details passed in class creation
    def __init__(self, email, password, sendToEmail, subject):
        self.email = email
        self.password = password
        self.sendToEmail = sendToEmail
        self.subject = subject

        self.msg = MIMEMultipart()
        self.msg["Subject"] = self.subject
        self.msg["From"] = self.email
        self.msg["To"] = self.sendToEmail

    # Sends the Email using the set variables
    def SendEmail(self):
        context = ssl.create_default_context()
        self.message = self.msg.as_string()
        print(self.email)
        print(self.password)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.sendToEmail, self.message)
            server.quit()

        print("Email Sent!")

    # Attaches a string variable to the Email
    def AttachText(self, text):
        self.msg.attach(MIMEText(text, "plain"))

    # Attaches a specified file to the Email
    def AttachFile(self, file):
        filename = file
        with open(filename, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
        encoders.encode_base64(part)

        part.add_header("Content-Disposition", f"attachment; filename= {filename}")

        self.msg.attach(part)

class Camera:
    # Set up basic Open_CV2 variables
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 24)
        self.cam.set(3, 1280)
        self.cam.set(4, 720)

        self.font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter("cameraCapture.mp4", self.fourcc, 24, (1280, 720))

    # Starts recording from the camera based on a certain time passed when the function is called
    def Record(self, recordTime):
        tick = 0
        print(f"Record Time: {recordTime}")

        while tick < recordTime * 100:
            self.ret, self.img = self.cam.read()

            self.img = cv2.flip(self.img, 0)
            tick += 1
            print(tick / 100)

        self.cam.release()
        cv2.destroyAllWindows()

class Accelerometer:
    def __init__(self):
        self.accel = msa301.MSA301()
        self.accel.reset()
        self.accel.set_power_mode('normal')

    def ReturnValue(self):
        firstx, firsty, firstz = self.accel.get_measurements()
        time.sleep(0.5)
        lastx, lasty, lastz = self.accel.get_measurements()
        
        finalx = firstx - lastx
        finaly = firsty - lasty
        finalz = firstz - lastz

        magnitude = math.sqrt(finalx * finalx + finaly * finaly + finalz * finalz)
        
        print(f'Movement magnitude: {magnitude}')
        return magnitude

class GPIODevices:
    class RGBLed:
        def __init__(self):
            self.pins = {'redPin':21, 'greenPin':20, 'bluePin':16}

        def SetColor(self, red, green, blue):
            GPIO.setmode(GPIO.BCM)

            if red == True:
                GPIO.setup(self.pins['redPin'], GPIO.OUT)
                GPIO.output(self.pins['redPin'], GPIO.HIGH)

            if green == True:
                GPIO.setup(self.pins['greenPin'], GPIO.OUT)
                GPIO.output(self.pins['greenPin'], GPIO.HIGH)

            if blue == True:
                GPIO.setup(self.pins['bluePin'], GPIO.OUT)
                GPIO.output(self.pins['bluePin'], GPIO.HIGH)

        def Off(self):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pins['redPin'], GPIO.OUT)
            GPIO.output(self.pins['redPin'], GPIO.LOW)
            GPIO.setup(self.pins['greenPin'], GPIO.OUT)
            GPIO.output(self.pins['greenPin'], GPIO.LOW)
            GPIO.setup(self.pins['bluePin'], GPIO.OUT)
            GPIO.output(self.pins['bluePin'], GPIO.LOW)
            GPIO.cleanup()

    class TempSensor:
        def __init__(self):
            self.SPI_PORT = 0
            self.SPI_DEV = 0
            self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEV))

        def ReturnValue(self, analogPort):
            raw = self.mcp.read_adc(analogPort)
            temp = ((raw * 330)/float(1023))-50
            temp = round(temp, 2)

            print(f'Temperature: {temp}')
            return temp

    class HeartSensor:
        def __init__(self):
            self.SPI_PORT = 0
            self.SPI_DEV = 0
            self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEV))

        def ReturnValue(self, analogPort):
            rate = self.mcp.read_adc(analogPort)

            print(f'Heart Rate: {rate}')
            return rate
