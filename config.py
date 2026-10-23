RANDOM_STATE = 42
N_SPLITS = 5            # stratified k-fold
DATA_PATH = "Data/arrhythmia.data"
CLEAN_PATH = "Data/clean_data.csv"
IMAGE_DIR = "Image/"

DROP_CLASS = 16         # "Others / unclassified"
NORMAL_CLASS = 1        # becomes label 0; classes 2-15 become label 1