import os
from glob import glob

import numpy as np
import pandas as pd
from tqdm import tqdm


def extract_dataFrame(feat_name):
    bin_files = glob(os.path.join(DATA_DIR, "features\\{}\\*.1min.bin".format(feat_name)))
    df_len = len(np.fromfile(bin_files[0]))
    col_names = [os.path.basename(path).split('.1min')[0] for path in bin_files]
    df = pd.DataFrame(np.zeros((df_len, len(bin_files))), columns=col_names)

    for bin_path in bin_files:
        col_name = os.path.basename(bin_path).split('.1min')[0]
        df[col_name] = np.fromfile(bin_path)

    return df


DATA_DIR = "C:\\Users\\hirva\\.qlib\\qlib_data\\cn_data_1min"

df_calendars = pd.read_csv(os.path.join(DATA_DIR, 'calendars', '1min.txt'), names=['0'])
df_instruments =
features = os.listdir(os.path.join(DATA_DIR, 'features'))

# feature_dict = {}
# for feature in tqdm(features):
#     df = extract_dataFrame(feature)
#     feature_dict[feature] = df

feature = features[0]
df = extract_dataFrame(feature)
