from bing_image_downloader import downloader

# ONLY the 10 classes you selected
diseases = {
    "acne": 150,
    "eczema": 150,
    "impetigo": 150,
    "melanoma": 150,
    "psoriasis": 150,
    "ringworm": 150,
    "rosacea": 150,
    "urticaria": 150,
    "vitiligo": 150,
    "warts": 150
}

for disease, count in diseases.items():
    downloader.download(
        disease + " skin disease",
        limit=count,
        output_dir="../dataset",
        adult_filter_off=False,
        force_replace=False,
        timeout=60
    )
    print(f"✅ Downloaded images for: {disease}")