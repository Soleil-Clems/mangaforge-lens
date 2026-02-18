import cv2 as cv


class MangaCleaner:
    def __init__(self, image_path: str):
        self.image = cv.imread(image_path)
        self.cleaned = self.image.copy()

    def clean_zone(self, zone: dict):
        x, y, w, h = zone["x"], zone["y"], zone["w"], zone["h"]
        self.cleaned[y:y+h, x:x+w] = 255

    def clean_all(self, zones: list):
        for zone in zones:
            self.clean_zone(zone)
        return self.cleaned

    def save(self, output_path: str):
        cv.imwrite(output_path, self.cleaned)
        print(f"Image sauvegardée : {output_path}")