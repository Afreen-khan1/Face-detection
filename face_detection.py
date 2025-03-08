
import cv2
import playsound 
from twilio.rest import Client
#add your sid,token,twilio number after creating account in twilio
account_sid ="Agjkhgfghgklkjbhbhmnj"
auth_token ="hjkjjhgyl877876"
twilio_number =+ #your twilio number
owner_phone_number =+ #your number followed by
client = Client(account_sid, auth_token)

def send_sms(message):
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=owner_phone_number
    )
print("SMS sent successfully")


def play_alarm_sound():
    playsound.playsound('alarm_sound.mp3')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

    if len(faces)>0:
     for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x, y),(x+w, y+h),(255,0,0),2)
        play_alarm_sound()
        send_sms("Face detected! Alarm triggered")

    cv2.imshow('Face Detection',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()