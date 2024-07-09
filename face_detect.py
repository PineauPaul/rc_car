import cv2
import sys


class FaceDetector():
    def __init__(self, camera_source, setting_file):
        self.camera_source = camera_source
        self.setting_file = setting_file
        self.plot = False

    def __del__(self):
        self.video_capture.release()
        cv2.destroyAllWindows()


    def camera_init(self):
        self.faceCascade = cv2.CascadeClassifier(self.setting_file)
        self.video_capture = cv2.VideoCapture(self.camera_source)

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