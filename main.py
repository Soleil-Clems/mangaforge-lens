from mangaforge_lens.detector import MangaDetector
from mangaforge_lens.ocr import MangaOCR
from mangaforge_lens.cleaner import MangaCleaner
from mangaforge_lens.translator import MangaTranslator
from mangaforge_lens.typesetter import MangaTypesetter

scan_path="tests/test_scan.jpg"
detector = MangaDetector(scan_path)
zones = detector.detect_text_zones()

print(f"{len(zones)} zones détectées")
for zone in zones:
    print(zone)

#detector.preview(zones)

ocr = MangaOCR(scan_path)
ocr_results = []
for zone in zones:
    result = ocr.read_text(zone)
    result["x"] = zone["x"]
    result["y"] = zone["y"]
    result["w"] = zone["w"]
    result["h"] = zone["h"]
    ocr_results.append(result)
    print(result)


cleaner = MangaCleaner(scan_path)
cleaner.clean_all(zones)
cleaner.save("tests/cleaned_scan.jpg")



translator = MangaTranslator(target_lang="en")
results = translator.translate_zones(ocr_results)
for r in results:
    print(r["original"], "→", r["translated"])


typesetter = MangaTypesetter("tests/cleaned_scan.jpg")
typesetter.apply(results)
typesetter.save("tests/final_scan.jpg")
