import config

import pandas as pd

from mlxtend.data import loadlocal_mnist

X, y = loadlocal_mnist(
        images_path='../input/t10k-images.idx3-ubyte',
        labels_path='../input/t10k-labels.idx1-ubyte')

# print(type(X))
# print(type(y))

print(X)
print(y)

pixel_columns = [f'pixel{i}' for i in range(len(X[0]))]
df = pd.DataFrame(X, columns=pixel_columns)
df.insert(0, 'label', y)

# print(df)

df.to_csv(config.TRAINING_FILE, index=False)