from mangaforge_lens.detector import MangaDetector

detector = MangaDetector("tests/test_scan.jpg")
zones = detector.detect_text_zones()

print(f"{len(zones)} zones détectées")
for zone in zones:
    print(zone)

detector.preview(zones)