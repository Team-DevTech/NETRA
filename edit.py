"""
import subprocess
from google.cloud import vision
import io
import time
import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BCM)

GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)

imagePath = "/home/pi/Desktop/netra/images/"
image = imagePath + "capture.jpg"
image1 = imagePath + "capture1.jpg"
def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()
    final = []
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    

    for text in texts:
        final.append(text.description.encode('utf-8'))
    return final

    
    
def detect_labels(path):
    """Detects labels in the file."""
    labelArray= []
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        val = label.description
        labelArray.append(val.encode("utf-8"))
    return labelArray
def labelfunc():
    """TODO: Set a trigger event"""
    #while True:
        #if button1=="pressed":
    """Button For Object Detection"""
    subprocess.call(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", image])
    recognizedObjects = detect_labels(image)
    str1 = ' '.join(recognizedObjects)
    strFinal = "There are " + str1 + " infront of you"
    print(str1)
    subprocess.call(["gtts-cli", strFinal , "--output", "/home/pi/Desktop/hello.mp3"])
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/hello.mp3"])
    """TODO: Pass this Above array in google text to speech code"""
        #if button2 =="pressed":
    """Execute OCR Script"""
def ocrfunc():
    time.sleep(2)
    subprocess.call(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", image1])
    ocrText = detect_text(image)
    str2 = ''.join(ocrText)
    strFinal2 = "There are " + str2 + " infront of you"
    subprocess.call(["gtts-cli", strFinal2 , "--output", "/home/pi/Desktop/hello.mp3"])
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/hello.mp3"])
if __name__ == "__main__":
    #while True:
        #PushButton0 = GPIO.input(19)
    while True:
        PushButton1 = GPIO.input(20)
        PushButton2 = GPIO.input(21)
        if PushButton1 == False:
            labelfunc()
            PushButton1 = True
        if PushButton2 == False:
            ocrfunc()
            PushButton2 = True

     
import subprocess
from google.cloud import vision
import io
import time
import RPi.GPIO as GPIO
from gtts import gTTS
import os

GPIO.setmode( GPIO.BCM)

GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)

imagePath = "/home/pi/Desktop/netra/images/"
image = imagePath + "capture.jpg"
image1 = imagePath + "capture1.jpg"
def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()
    final = []
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    

    for text in texts:
        final.append(text.description.encode('utf-8'))
    return final

    
    
def detect_labels(path):
    """Detects labels in the file."""
    labelArray= []
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        val = label.description
        labelArray.append(val.encode("utf-8"))
    return labelArray
def labelfunc():
    """TODO: Set a trigger event"""
    #while True:
        #if button1=="pressed":
    """Button For Object Detection"""
    subprocess.call(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", image])
    recognizedObjects = detect_labels(image)
    str1 = ' '.join(recognizedObjects)
    #strFinal = "There are " + str1 + " infront of you"
    print(str1)
    #subprocess.call(["gtts-cli", strFinal , "--output", "/home/pi/Desktop/hello.mp3"])
    #subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/hello.mp3"])
    myObj = gTTS ( text= "Things in front of you are " + str1 , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/netra/hello.mp3"])

    """TODO: Pass this Above array in google text to speech code"""
        #if button2 =="pressed":
    """Execute OCR Script"""
def ocrfunc():
    #time.sleep(2)
    subprocess.call(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", image1])
    ocrText = detect_text(image1)
    str2 = ''.join(ocrText)
    #strFinal2 = "There are " + str2 + " infront of you"
    myObj = gTTS ( text= "The text written in front of you is " + str2 + " infront of you" , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#   subprocess.call(["gtts-cli", strFinal2 , "--output", "/home/pi/Desktop/hello.mp3"])
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/netra/hello.mp3"])
if __name__ == "__main__":
    myObj = gTTS ( text= "Welcome to netra by devtech" , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/netra/hello.mp3"])
    flag = False
    while True:
        PushButton0 = GPIO.input(19)
        while PushButton0 == False:
            print("YOU'RE ACTIVE")
            PushButton1 = GPIO.input(20)
            PushButton2 = GPIO.input(21)
            if PushButton1 == False:
                print("OBJECT DETECTION ACTIVE")
                labelfunc()
                while PushButton1 == False:
                    PushButton1 = GPIO.input(20)
            PushButton0 = GPIO.input(19)
            if PushButton0 == True:
                    flag = True
                    break
            if PushButton2 == False:
                print("OCR ACTIVE")
                ocrfunc()
                while True:
                    PushButton2 = GPIO.input(21)
                    if PushButton2 == True:
                        break
            PushButton0 = GPIO.input(19)
            if PushButton0 == True:
                flag = True
                break
        if flag == True:
            break
    print("CONNECTION CLOSED!")
    myObj = gTTS ( text= "Thanks for using netra by devtech" , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/netra/hello.mp3"])
"""
 import subprocess
from google.cloud import vision
import io
import time
import RPi.GPIO as GPIO
from gtts import gTTS
import os

GPIO.setmode( GPIO.BCM)

GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)

imagePath = "/home/pi/Desktop/netra/images/"
image = imagePath + "capture.jpg"
image1 = imagePath + "capture1.jpg"
def detect_text(path):
    """Detects text in the file."""
    try:
        client = vision.ImageAnnotatorClient()
        final = []
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        

        for text in texts:
            final.append(text.description.encode('utf-8'))
        return final
    except:
        return final
    
def detect_labels(path):
    """Detects labels in the file."""
    labelArray= []
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        val = label.description
        labelArray.append(val.encode("utf-8"))
    return labelArray
def labelfunc():
    """TODO: Set a trigger event"""
    #while True:
        #if button1=="pressed":
    """Button For Object Detection"""
    subprocess.call(["fswebcam", "-r", "640x480", "--no-banner", "--jpeg", "85", "-D", "1", image])
    recognizedObjects = detect_labels(image)
    str1 = ' '.join(recognizedObjects)
    #strFinal = "There are " + str1 + " infront of you"
    print(str1)
    #subprocess.call(["gtts-cli", strFinal , "--output", "/home/pi/Desktop/hello.mp3"])
    #subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/hello.mp3"])
    myObj = gTTS ( text= "Things in front of you are " + str1 + ", , " , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["omxplayer", "--no-keys", "/home/pi/Desktop/netra/hello.mp3", " $ "])

    """TODO: Pass this Above array in google text to speech code"""
        #if button2 =="pressed":
    """Execute OCR Script"""
def ocrfunc():
    #time.sleep(2)
    subprocess.call(["fswebcam", "-r", "640x480", "--no-banner",  "--jpeg", "85", "-D", "1", image1])
    ocrText = detect_text(image1)
    str2 = ''.join(ocrText)
    first_half=len(str2)
    print(str2[0:first_half/2])
    #strFinal2 = "There are " + str2 + " infront of you"
    myObj = gTTS ( text= "The text written in front of you is " + str2[0:first_half/2] + ", , " , lang = 'en', slow = False)
    try:
        myObj.save("/home/pi/Desktop/netra/hello.mp3")
    except:
        myObj = gTTS ( text= "The text written in front of you is " + str2[0:(first_half/2)-5] + ", , " , lang = 'en', slow = False)
        myObj.save("/home/pi/Desktop/netra/hello.mp3")
#   subprocess.call(["gtts-cli", strFinal2 , "--output", "/home/pi/Desktop/hello.mp3"])
    subprocess.call(["omxplayer", "--no-keys", "/home/pi/Desktop/netra/hello.mp3", " $ "])
if __name__ == "__main__":
    #myObj = gTTS ( text= "Welcome to netra by devtech, press the top most key to enter the system, middle key for object detection, and, bottom key for text recognition, you're good to start now." , lang = 'en', slow = False)
    #myObj.save("/home/pi/Desktop/netra/begin.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["omxplayer", "--no-keys", "/home/pi/Desktop/netra/begin.mp3", " $ "])
    flag = False
    PushButton0 = True
    while True:
        PushButton0 = GPIO.input(19)
        while PushButton0 == False:
            print("YOU'RE ACTIVE")
            PushButton1 = GPIO.input(20)
            PushButton2 = GPIO.input(21)
            if PushButton1 == False:
                print("OBJECT DETECTION ACTIVE")
                labelfunc()
                while PushButton1 == False:
                    PushButton1 = GPIO.input(20)
            PushButton0 = GPIO.input(19)
            if PushButton0 == True:
                    flag = True
                    break
            if PushButton2 == False:
                print("OCR ACTIVE")
                ocrfunc()
                while True:
                    PushButton2 = GPIO.input(21)
                    if PushButton2 == True:
                        break
            PushButton0 = GPIO.input(19)
            if PushButton0 == True:
                flag = True
                break
        if flag == True:
            break
    print("CONNECTION CLOSED!")
    #myObj = gTTS ( text= "Thanks for using netra by Devtech, have a nice day." , lang = 'en', slow = False)
    #myObj.save("/home/pi/Desktop/netra/credit.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["omxplayer", "--no-keys", "/home/pi/Desktop/netra/credit.mp3", " $ "])





