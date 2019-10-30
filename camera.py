import cv2
import pafy

url = 'https://youtu.be/25EgbhdVESE'
vPafy = pafy.new(url)
play = vPafy.getbest()


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(play.url)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
