import os
import shutil
import pandas as pd

# ✅ Actual paths for your machine
csv_path = r"C:\Users\Vivek\Landscape-Image-Classifier\raw_images\train.csv"
image_folder = r"C:\Users\Vivek\Landscape-Image-Classifier\raw_images\train"
output_base = r"C:\Users\Vivek\Landscape-Image-Classifier\organized_images"

# Load CSV
df = pd.read_csv(csv_path)

# Create class folders and move files
for _, row in df.iterrows():
    img_name = row['image_name']
    label = str(row['label'])

    src = os.path.join(image_folder, img_name)
    dst_dir = os.path.join(output_base, label)
    dst = os.path.join(dst_dir, img_name)

    os.makedirs(dst_dir, exist_ok=True)
    
    if os.path.exists(src):
        shutil.copy(src, dst)  # Use shutil.move() if you want to move instead of copy
    else:
        print(f"❌ Image not found: {src}")

print("✅ Images organized successfully into folders!")
