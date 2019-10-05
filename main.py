"""
import subprocess
from google.cloud import vision
import io
import time

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
    time.sleep(4)
    subprocess.call(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", image1])
    ocrText = detect_text(image)
    str2 = ''.join(ocrText)
    strFinal2 = "There are " + str2 + " infront of you"
    subprocess.call(["gtts-cli", strFinal2 , "--output", "/home/pi/Desktop/hello.mp3"])
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/hello.mp3"])
if __name__ == "__main__":
    labelfunc()
    ocrfunc()
"""
import subprocess
from google.cloud import vision
import io
import time
from gtts import gTTS
import os

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
     #print(texts)
 
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
    #time.sleep(4)
    subprocess.call(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", image1])
    ocrText = detect_text(image1)
    str2 = ''.join(ocrText)
    #strFinal2 = "There are " + str2 + " infront of you"
    myObj = gTTS ( text= "The Text written in front of you is " + str2 + " thank you" , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#     subprocess.call(["gtts-cli", strFinal2 , "--output", "/home/pi/Desktop/hello.mp3"])
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/netra/hello.mp3"])
if __name__ == "__main__":
    myObj = gTTS ( text= "Welcome to netra by devtech" , lang = 'en', slow = False)
    myObj.save("/home/pi/Desktop/netra/hello.mp3")
#     os.system("mpg321 hello.mp3")
    subprocess.call(["vlc", "--vout", "none", "/home/pi/Desktop/netra/hello.mp3"])
    labelfunc()
    ocrfunc()




