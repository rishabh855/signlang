import os

# Root project folder
root = "C:\\Users\\Rishabh\\Desktop\\SignLang"

# Folder structure
folders = [
    "datasets/dataset_raw/ISL_Dataset",
    "datasets/dataset_processed",
    "models",
    "backend",
    "frontend/public",
    "frontend/src",
    "scripts"
]

# Create folders
for folder in folders:
    path = os.path.join(root, folder)
    os.makedirs(path, exist_ok=True)
    print(f"Created: {path}")

# Create empty starter files
starter_files = [
    "backend/app.py",
    "backend/train_model.py",
    "backend/utils.py",
    "backend/requirements.txt",
    "frontend/src/App.js",
    "frontend/src/index.js",
    "frontend/src/styles.css",
    "frontend/public/index.html",
    "scripts/preprocess_dataset.py",
    "README.md"
]

for file in starter_files:
    path = os.path.join(root, file)
    with open(path, "w") as f:
        pass
    print(f"Created file: {path}")

print("\n✅ Project folder structure created successfully!")
