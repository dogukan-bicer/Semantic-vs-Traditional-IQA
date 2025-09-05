# NITE-IQA-Semantic-Image-Similarity

This repository contains the implementation and experiments from the paper:  

**"Comprehensive Comparison of Semantic Image Similarity Analysis Techniques with Traditional Methods using the NITE-IQA Dataset"**  
*Doğukan Biçer, Marmara University, Istanbul, Türkiye*  

---

## 🚀 Overview

Image similarity analysis aims to quantify the similarity between two images.  
In this project, we perform a **comprehensive evaluation** of semantic similarity methods (DINOv2, DISTS, OpenCLIP) against the traditional **SSIM metric** on the **NITE-IQA dataset**.  

A custom **evaluation pipeline** and **interactive Tkinter-based GUI** were developed to compare metrics both quantitatively and qualitatively.  

Key findings:  
- Semantic metrics show **higher correlation with human subjective scores (MOS)**  
- Semantic metrics are more robust to low-level distortions (blur, noise, compression)  
- Traditional SSIM often fails to capture **semantic content preservation**  

---

## 📂 Project Structure

NITE-IQA-Semantic-Image-Similarity/
│
├── main.py # Entry point: starts the Tkinter GUI
├── README.md # Project documentation
│
├── utils/ # Helper functions
│ ├── csv_utils.py
│ └── correlation_utils.py
│
├── quality/ # Image quality & similarity metrics
│ └── image_quality.py
│
└── ui/ # GUI components
└── compare_table.py


---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/NITE-IQA-Semantic-Image-Similarity.git
cd NITE-IQA-Semantic-Image-Similarity

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

📊 Usage

Run the GUI:

python main.py


Select Reference Folder and Distorted Folder

Click Start → Matching images are compared using all metrics

Optionally load a MOS Excel file for correlation analysis

Save results to CSV or export them to Excel

📦 Dependencies

Python 3.9+

Tkinter

PyTorch

HuggingFace Transformers

OpenCLIP

DISTS-pytorch

scikit-image

Pandas

OpenPyXL

📖 Example Output

GUI Table: Thumbnails of reference & distorted images with similarity scores

Excel Export:

Sheet 1: Full comparison results + MOS

Sheet 2: Correlation summary (PLCC, RMSE, SROCC, KROCC)

👩‍💻 Authors

Developed by Doğukan Biçer
Marmara University, Department of Electrical and Electronics Engineering