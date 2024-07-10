from motor import Motor
from servo import Servo
from face_detect import FaceDetector


class CarManager():
    def __init__(self):
        self.state = [0,0,0] #X,Y,theta
        self.face_detector = FaceDetector(0,"haarcascade_frontalface_default.xml")
        self.servo = Servo()
        self.motor = Motor()

    def get_face_target(self):
        resolution = self.face_detector.get_resolution()
        for (x, y, w, h) in self.face_detector.detect_face():
            errx = (resolution[0]/2) - x
            erry = (resolution[1]/2) - y

            dist = (w*h)/(resolution[0]*resolution[1])

        return errx,erry,dist

    # def regulate(self):


if __name__=="__main__":
    print('Run car manager')