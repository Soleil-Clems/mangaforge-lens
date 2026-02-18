import pytesseract
from manga_ocr import MangaOcr
from langdetect import detect
from PIL import Image
import cv2 as cv


class MangaOCR:
    def __init__(self, image_path: str):
        self.image = cv.imread(image_path)
        self.manga_ocr = MangaOcr()

    def extract_zone(self, zone: dict):
        x, y, w, h = zone["x"], zone["y"], zone["w"], zone["h"]
        cropped = self.image[y:y + h, x:x + w]
        return cropped

    def read_text(self, zone: dict):
        cropped = self.extract_zone(zone)
        pil_image = Image.fromarray(cv.cvtColor(cropped, cv.COLOR_BGR2RGB))

        text = pytesseract.image_to_string(pil_image).strip()

        if not text:
            text = self.manga_ocr(pil_image)

        try:
            language = detect(text)
        except:
            language = "unknown"

        return {
            "text": text,
            "language": language
        }