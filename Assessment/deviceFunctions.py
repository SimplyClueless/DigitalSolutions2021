# Database Module
import mysql.connector

# Email modules
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

# Raspberry PI GPIO Modules
try:
    import RPi.GPIO as GPIO 
except:
    pass

class database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.connection.cursor(buffered=True)

    # Prints all the tables in the connected database
    def showTables(self):
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        for table in result:
            print(table)

    # Print all the variables in the defined table
    def showVariables(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        columns = [tuple[0] for tuple in self.cursor.description]
        print(columns)

    # SELECT "" FROM ""
    def returnData(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for value in result:
            print(value)

    # INSERT INTO "" (var, var) VALUES (%s, %s)
    def importData(self, query, values):
        self.cursor.execute(query, values)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

class Email:
    
    def __init__(self, email, password, sendToEmail, subject):
        self.email = email
        self.password = password
        self.sendToEmail = sendToEmail
        self.subject = subject

        self.msg = MIMEMultipart()
        self.msg["Subject"] = self.subject
        self.msg["From"] = self.email
        self.msg["To"] = self.sendToEmail

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

    def AttachText(self, text):
        self.msg.attach(MIMEText(text, "plain"))

    def AttachFile(self, file):
        filename = file
        with open(filename, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
        encoders.encode_base64(part)

        part.add_header("Content-Disposition", f"attachment; filename= {filename}")

        self.msg.attach(part)

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 30)
        self.cam.set(3, 1280)
        self.cam.set(4, 720)

        self.font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter("roomCapture.avi", self.fourcc, 30, (1280, 720))

    def Record(self, recordTime):
        tick = 0

        while tick < recordTime * 10:
            self.ret, self.img = self.cam.read()

            self.img = cv2.flip(self.img, 0)
            cv2.putText(self.img, "You're being recorded", (400, 100), self.font, 2, (0, 83 ,207), 2, cv2.LINE_AA)
            cv2.putText(self.img, str(datetime.now()), (1000, 700), self.font, .5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('Security Camera', self.iSmg)

            self.out.write(self.img)
            tick += 1
            print(tick)

        self.cam.release()
        cv2.destroyAllWindows()

class Accelerometer:
    pass

class Buzzer:
    def __init__(self, buzzer):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.buzzer = buzzer

        GPIO.setup(self.buzzer, GPIO.OUT)
    
    def On(self):
        GPIO.output(self.buzzer, GPIO.HIGH)

    def Off(self):
        GPIO.output(self.buzzer, GPIO.LOW)

    def Beep(self, delay):
        self.On()
        time.sleep(delay)
        self.Off()
        time.sleep(delay)