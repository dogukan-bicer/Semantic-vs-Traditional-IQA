# NITE-IQA-Semantic-Image-Similarity

Implementation and experiments for the paper:

**Comprehensive Comparison of Semantic Image Similarity Analysis Techniques with Traditional Methods using the NITE-IQA Dataset**
*Doğukan Biçer — Marmara University, İstanbul, Türkiye*

---

## 🚀 Overview

This repository contains the code, evaluation pipeline and an interactive GUI used to compare **semantic** image similarity methods (DINOv2, DISTS, OpenCLIP) against the traditional **SSIM** metric on the **NITE-IQA** dataset.

Features:

* Reproducible evaluation pipeline for objective metric calculation and MOS matching
* Tkinter-based interactive GUI for qualitative inspection and error analysis
* Export of results to CSV / Excel and correlation summary (PLCC, SROCC, KROCC, RMSE)

Key findings (from experiments):

* Semantic metrics correlate better with human MOS scores
* Semantic metrics are more robust to many low-level distortions (noise, blur, compression)
* SSIM often fails to capture semantic content preservation

---

## 📁 Repository structure

```
NITE-IQA-Semantic-Image-Similarity/
├── main.py                 # Entry point: launches the Tkinter GUI
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── utils/                  # Helper modules
│   ├── csv_utils.py
│   └── correlation_utils.py
├── quality/                # Image quality / similarity metric implementations
│   └── image_quality.py
└── ui/                     # GUI components
    └── compare_table.py
```

---

## 🛠️ Installation

**Recommended:** use a Python virtual environment.

```bash
# 1) Clone the repository
git clone https://github.com/dogukan-bicer/Semantic-vs-Traditional-IQA.git
cd Semantic-vs-Traditional-IQA

# 2) Create and activate a virtual environment
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
# venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt
```

**Notes:**

* Tested with Python 3.9+ and PyTorch (see `requirements.txt` for exact versions).
* If you use GPU, install the appropriate `torch` build for your CUDA version.

---

## ▶️ Usage

Run the GUI:

```bash
python main.py
```

GUI workflow:

1. Select **Reference Folder** (folder with clean/reference images)
2. Select **Distorted Folder** (folder with distorted/received images)
3. (Optional) Load an Excel/CSV file with MOS scores for correlation analysis
4. Click **Start** — matching images are compared with all implemented metrics
5. Save results as CSV / export to Excel

Command-line (non-GUI) usage (example helper script provided in `utils/`):

```bash
python utils/run_metrics.py --ref ./data/ref --dist ./data/dist --out results.csv
```

---

## 📦 Dependencies

* Python 3.9+
* Tkinter (for GUI)
* PyTorch
* HuggingFace Transformers
* OpenCLIP (or `open_clip_torch`)
* `dists-pytorch` (or local implementation)
* scikit-image
* pandas
* openpyxl

Exact versions and additional packages are listed in `requirements.txt`.

---

## 📖 Datasets and Citations

Please cite the datasets and core methods used in this work if you reuse the code or results.

**NITE-IQA / NITS-IQA (dataset used in the paper):**
Ruikar, J. and Chaudhury, S., "NITS‑IQA Database: A New Image Quality Assessment Database," *Sensors*, vol. 23, no. 4, art. 2279, Feb. 2023. doi:10.3390/s23042279.

**LIVE-MD dataset** (if used): Jayaraman, D., Mittal, A., Moorthy, A.K., Bovik, A.C., "LIVE Multiply Distorted Image Quality Database (LIVE-MD)." \[Online]. Available: [http://live.ece.utexas.edu/research/Quality/live\_multidistortedimage.html](http://live.ece.utexas.edu/research/Quality/live_multidistortedimage.html)

**Core methods referenced in the project:**

* Zhang, Isola, Efros — LPIPS (CVPR 2018).
* Wang et al. — SSIM (IEEE TIP, 2004).
* Ding et al. — DISTS (arXiv:2004.07728, 2020).
* Oquab et al. — DINOv2 (arXiv:2304.07193, 2023).
* Radford et al. — CLIP (ICML 2021).

Add these citations to your paper or presentations where relevant.

---

## 🧪 Example outputs

* GUI table with thumbnails and per-metric similarity scores
* Excel exports containing:

  * Sheet 1: full comparison + MOS
  * Sheet 2: correlation summary (PLCC, SROCC, KROCC, RMSE)

Screenshots and sample exported files are available in the `examples/` folder (if present).

---


*Last updated: Sep 7, 2025*
