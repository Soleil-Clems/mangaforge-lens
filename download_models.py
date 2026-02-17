from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="ogkalu/comic-speech-bubble-detector-yolov8m",
    filename="comic-speech-bubble-detector.pt",
    local_dir="models/"
)