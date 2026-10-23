
# Arrhythmia Classification

Binary classification of normal heartbeats and arrhythmia using the UCI Arrhythmia dataset.

## Team
- Medha — Data preprocessing and selected machine learning models
- Akshitaa — Exploratory data analysis and selected machine learning models

## Project Structure
- `Data/` — Raw and cleaned datasets
- `Preprocessing and EDA/` — Preprocessing and exploratory analysis notebooks
- `Model/` — Model training and PCA experiments
- `Image/` — Figures for the report and presentation
- `Reports/` — Final report and presentation

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Labels
- 0 — Normal (original class 1)
- 1 — Arrhythmia (original classes 2–15)
- Original class 16 is excluded.

## Cross-validation
Stratified 5-fold cross-validation with random_state=42.
