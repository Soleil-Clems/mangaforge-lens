from deep_translator import GoogleTranslator


class MangaTranslator:
    def __init__(self, target_lang: str = "en"):
        self.target_lang = target_lang

    def translate(self, text: str, source_lang: str = "auto"):
        if not text.strip():
            return ""

        translated = GoogleTranslator(
            source=source_lang,
            target=self.target_lang
        ).translate(text)

        return translated

    def translate_zones(self, zones_text: list):
        results = []
        for item in zones_text:
            translated = self.translate(item["text"])
            results.append({
                "original": item["text"],
                "translated": translated,
                "language": item["language"],
                "x": item["x"],
                "y": item["y"],
                "w": item["w"],
                "h": item["h"]
            })
        return results