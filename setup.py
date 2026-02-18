from setuptools import setup, find_packages

setup(
    name="mangaforge-lens",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "Pillow",
        "numpy",
        "manga-ocr",
        "pytesseract",
        "langdetect",
        "deep-translator",
        "ultralytics",
        "huggingface_hub",
    ],
    author="Soleil OUISOL",
    description="Manga scan reading, OCR, translation and typesetting library",
    python_requires=">=3.8",
)