from ultralytics import YOLO
import cv2 as cv


class MangaDetector:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = cv.imread(image_path)
        self.model = YOLO("models/comic-speech-bubble-detector.pt")

        if len(self.image.shape) == 2:
            self.gray = self.image
        else:
            self.gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

    def detect_text_zones(self):
        results = self.model(self.image_path)

        zones = []
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            confidence = box.conf[0].item()

            if confidence > 0.5:
                zones.append({
                    "x": int(x1),
                    "y": int(y1),
                    "w": int(x2 - x1),
                    "h": int(y2 - y1),
                    "confidence": round(confidence, 2)
                })

        return zones

    def preview(self, zones):
        preview_image = self.image.copy()
        for zone in zones:
            x, y, w, h = zone["x"], zone["y"], zone["w"], zone["h"]
            cv.rectangle(preview_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv.imshow("MangaForge Lens - Detection", preview_image)
        cv.waitKey(0)
        cv.destroyAllWindows()