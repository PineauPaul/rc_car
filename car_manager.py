from motor import Motor
from servo import Servo
from face_detect import FaceDetector

class CarManager():
    def __init__(self):
        self.state = [0,0,0] #X,Y,theta
        self.face_detector = FaceDetector(0,"haarcascade_frontalface_default.xml")
        self.servo = Servo()
        self.motor = Motor()

    
if __name__=="__main__":
    print('Run car manager')