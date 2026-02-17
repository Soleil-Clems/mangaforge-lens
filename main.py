from mangaforge_lens.detector import MangaDetector
from mangaforge_lens.ocr import MangaOCR

scan_path="tests/test_scan.jpg"
detector = MangaDetector(scan_path)
zones = detector.detect_text_zones()

print(f"{len(zones)} zones détectées")
for zone in zones:
    print(zone)

#detector.preview(zones)

ocr = MangaOCR(scan_path)
print("Ocr denut")
for zone in zones:
    result = ocr.read_text(zone)
    print(result)