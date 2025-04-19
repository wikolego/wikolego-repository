# Import required libraries
import config
import pandas as pd
from mlxtend.data import loadlocal_mnist

import config

# Load data from files
X, y = loadlocal_mnist(
        images_path=config.DOWNLOADED_IMAGES_PATH,
        labels_path=config.DOWNLOADED_LABELS_PATH
)

# Add labels and columns
pixel_columns = [f"pixel{i}" for i in range(len(X[0]))]
df = pd.DataFrame(X, columns=pixel_columns)
# df.insert(0, "label", y)
df["label"] = y

# Save data to file
df.to_csv(config.BASIC_DATA_PATH, index_label="id")