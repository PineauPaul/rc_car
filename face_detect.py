import cv2
import sys
import time


class FaceDetector():
    def __init__(self, camera_source, setting_file):
        self.camera_source = camera_source
        self.setting_file = setting_file
        self.plot = False
        self.resolution = (640,480)

    def __del__(self):
        self.video_capture.release()
        cv2.destroyAllWindows()


    def camera_init(self):
        self.faceCascade = cv2.CascadeClassifier(self.setting_file)
        self.video_capture = cv2.VideoCapture(self.camera_source)
        print("Width = ", self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        print("Height = ", self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.resolution = (self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH),self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_resolution(self):
        return self.resolution

    def set_plot(self, value):
        self.plot = value

    def detect_face(self):
        ret, frame = self.video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        print(faces)
        if (self.plot):
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)
        return faces

if __name__ == "__main__":
    FD = FaceDetector(0,sys.argv[1])
    FD.set_plot(True)
    FD.camera_init()
    while True:
        FD.detect_face()