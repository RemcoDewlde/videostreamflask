import cv2
import pafy

url = 'https://youtu.be/'


class VideoCamera(object):
    def __init__(self, vidID):
        vPafy = pafy.new(url + vidID)
        play = vPafy.getbest()
        self.video = cv2.VideoCapture(play.url)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
