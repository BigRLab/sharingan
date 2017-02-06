import sys

import cv2

from tesseract import Tesseract
from constants import WINDOW, POINT_COLOR


class Image:

    class THRESHOLD:
        MEAN = cv2.ADAPTIVE_THRESH_MEAN_C
        GAUSSIAN = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        IMG_PATH = 'image_processed.jpg'
        WINDOW = 'threshold'
        TRACK_BLOCK = 'block_size'
        TRACK_C = 'constant'
        BLOCK_SIZE_RANGE = [1, 9]
        C_RANGE = [1, 10]

        # OpenCV 3.2 doesn't allow parameters in callback so globals
        thresh_type = GAUSSIAN
        block_size = 3
        c = 2

    def __init__(self, image: str, *args, **kwargs):
        self.image = cv2.imread(image, 0)

    def threshold(self, thresh_type: int, block_size: int, c: int,
                  callback=False, **kwargs):
        """
        Threshold image

        :param thresh_type: mean/gaussian adaptive thresholding
        :param block_size: Size of a pixel neighborhood that is used to
                           calculate a threshold value for the pixel: 3, 5, 7,
                           and so on.
        :param c: constant subtracted from the mean or weighted mean
        :returns: thresholded image
        """
        self.thresh_type = thresh_type
        img = cv2.medianBlur(self.image, 5)

        thresh_img = cv2.adaptiveThreshold(img, 255, thresh_type,
                                           cv2.THRESH_BINARY, block_size, c)

        # Temporary jugaad
        cv2.imwrite(Image.THRESHOLD.IMG_PATH, thresh_img)

        return thresh_img

    def transform(self, *args, **kwargs):
        raise NotImplementedError

    def crop(self, *args, **kwargs):
        raise NotImplementedError

    def get_text(self, *args, **kwargs) -> str:
        """
        Extract text from thresholded image

        :param: None
        :returns: text extracted
        """
        tess_obj = Tesseract(Image.THRESHOLD.IMG_PATH)
        text = tess_obj.get_text()

        return text

    def resize(self, resize_by: int, *args, **kwargs):
        """
        Resize large dimesion images

        :param img: Large dimension image to be resized
        :returns: resized image
        """
        new_x, new_y = self.image.shape[1] // resize_by, \
                       self.image.shape[0] // resize_by

        self.image = cv2.resize(self.image, (new_x, new_y))

    def show_thresh(self, thresh_img=None, *args, **kwargs):
        """
        Prepare image window and show image

        :param img: Default thresholded image
        :returns: None
        """
        c = Image.THRESHOLD
        cv2.namedWindow(c.WINDOW)
        cv2.createTrackbar(c.TRACK_BLOCK, c.WINDOW, c.BLOCK_SIZE_RANGE[0],
                           c.BLOCK_SIZE_RANGE[1], self._callback_thresh)
        cv2.createTrackbar(c.TRACK_C, c.WINDOW, c.C_RANGE[0], c.C_RANGE[1],
                           self._callback_thresh)
        if thresh_img is None:
            thresh_img = self.image

        while True:
            cv2.imshow(c.WINDOW, thresh_img)
            self._wait_key(1, c.WINDOW)

    def show_image(self, *args, **kwargs):
        """
        Show original image image
        """
        cv2.namedWindow(WINDOW)
        cv2.setMouseCallback(WINDOW, self._mouse_click_callback)
        while True:
            cv2.imshow(WINDOW, self.image)
            self._wait_key(20, WINDOW)

    def _callback_thresh(self, preset: int, *args, **kwargs):
        """
        Trackbar change callback

        :param preset: preset value from trackbar
        :returns: None
        """
        t = Image.THRESHOLD

        # get preset odd value
        t.block_size = cv2.getTrackbarPos(t.TRACK_BLOCK, t.WINDOW)*2 + 1
        t.c = cv2.getTrackbarPos(t.TRACK_C, t.WINDOW)

        thresh_image = self.threshold(thresh_type=t.thresh_type, callback=True,
                                      block_size=t.block_size, c=t.c)
        self.show_thresh(thresh_image)

    def _mouse_click_callback(self, event: int, x: int, y: int, *args,
                              **kwargs):
        """
        Mouse event callback

        :param event: event integer value
        :param x: coordinate x value
        :param y: coordinate y value
        :returns: None
        """
        if event == cv2.EVENT_LBUTTONUP:
            cv2.circle(self.image, (x, y), 4, POINT_COLOR, -1)

    def _wait_key(self, k: int, window: str, type=None, *args, **kwargs):
        """
        Wrapper around cv2.waitKey

        :param k: delay in ms
        :param window: windo name
        :param type: window type (TODO: WHY ?)
        :returns: None
        """
        k = cv2.waitKey(k) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
        elif k == 13:
            pass

