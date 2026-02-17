from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
import numpy as np


class MangaTypesetter:
    def __init__(self, cleaned_image_path: str):
        self.image = Image.open(cleaned_image_path).convert("RGB")
        self.draw = ImageDraw.Draw(self.image)

    def _fit_text(self, text: str, zone: dict, font_path=None):
        max_w, max_h = zone["w"] - 10, zone["h"] - 10
        font_size = 20

        while font_size > 6:
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
            lines = self._wrap_text(text, font, max_w)
            total_h = len(lines) * (font_size + 2)
            if total_h <= max_h:
                return font, lines
            font_size -= 1

        return ImageFont.load_default(), self._wrap_text(text, ImageFont.load_default(), max_w)

    def _wrap_text(self, text: str, font, max_width: int):
        words = text.split()
        lines = []
        current = ""

        for word in words:
            test = f"{current} {word}".strip()
            bbox = font.getbbox(test)
            if bbox[2] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word

        if current:
            lines.append(current)
        return lines

    def write_zone(self, zone: dict, text: str, font_path=None):
        font, lines = self._fit_text(text, zone, font_path)
        font_size = font.size if hasattr(font, "size") else 10
        total_h = len(lines) * (font_size + 2)

        x = zone["x"] + zone["w"] // 2
        y = zone["y"] + (zone["h"] - total_h) // 2

        for line in lines:
            bbox = font.getbbox(line)
            line_w = bbox[2]
            self.draw.text((x - line_w // 2, y), line, fill="black", font=font)
            y += font_size + 2

    def apply(self, translated_zones: list, font_path=None):
        for item in translated_zones:
            if item["translated"]:
                self.write_zone(item, item["translated"], font_path)
        return self.image

    def save(self, output_path: str):
        self.image.save(output_path)
        print(f"Image finale sauvegardée : {output_path}")