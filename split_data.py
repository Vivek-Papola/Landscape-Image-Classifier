import os, random, shutil

src = "data/train"
splits = {"train":0.7, "val":0.15, "test":0.15}
base = "data"

# Make target dirs
for sp in splits:
    for cls in os.listdir(src):
        os.makedirs(os.path.join(base, sp, cls), exist_ok=True)

# Split per class
for cls in os.listdir(src):
    imgs = os.listdir(os.path.join(src, cls))
    random.shuffle(imgs)
    n = len(imgs)
    start = 0
    for sp, frac in splits.items():
        end = start + int(frac * n)
        for img in imgs[start:end]:
            shutil.move(os.path.join(src, cls, img),
                        os.path.join(base, sp, cls, img))
        start = end
