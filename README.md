# License-plate-identification

## Summary
This project uses the [License Plate Recognition Dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e?utm_source=chatgpt.com) from Roboflow 
The goal is to detect vehicle license plates (object detection) so you can integrate into downstream tasks like OCR, parking management, toll systems, or traffic monitoring.


## 📋 Dataset

- **Dataset Name**: License Plate Recognition (Project ID: `license-plate-recognition-rxg4e`) on Roboflow Universe. [Roboflow+2Roboflow+2](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e?utm_source=chatgpt.com)
    
- **Dataset Link**: [https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e?utm_source=chatgpt.com)
    
- **Total Images**: ~10,125 images (in one version) [Roboflow+1](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4?utm_source=chatgpt.com)
    
- **Split**:

    A custom split was done as follows :
    
    - Training: ~7,083 images (≈ 70%) [Roboflow+1](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4?utm_source=chatgpt.com)
        
    - Validation: 1,521 images (≈ 15%) [Roboflow](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4?utm_source=chatgpt.com)
        
    - Test: 1,521 images (≈ 15%) [Roboflow](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4?utm_source=chatgpt.com)

- **Classes**:

    - `License_Plate` (1 class) [Roboflow](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e?utm_source=chatgpt.com)
    
## How to Run

Clone the repository

```
git clone <your_repo_url>

cd <your_repo_folder>
```

## Project structure
```
├── environment.yml           # Conda environment definition
├── data/                     # Dataset folder (after download)
│   ├── train/
│   ├── val/
│   └── test/
├── models/
│   └── yolo-M.pt             # Pretrained / starting weights
├── train.py                  # Script to train the model
├── infer.py                  # Script to run inference
├── README.md                 # This file
└── results/                  # Output folders: weights, logs, etc
```

<!-- TODO add images and ocr steps -->