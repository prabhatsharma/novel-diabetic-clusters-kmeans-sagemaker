import argparse
import os
import warnings

import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
# import joblib
from sklearn.externals import joblib

if __name__=='__main__':
    parser = argparse.ArgumentParser()
#     parser.add_argument('--train-test-split-ratio', type=float, default=0.3)
#     args, _ = parser.parse_known_args()
    
#     print('Received arguments {}'.format(args))

    input_data_path = os.path.join('/opt/ml/processing/input', 'diabetes_data.csv')
    output_path = os.path.join('/opt/ml/processing/train', 'diabetes_data_transformed.csv')
    scaler_output_path = os.path.join('/opt/ml/processing/scaler', 'scaler.gz')
    
    data = pd.read_csv(input_data_path)
    
    scaler = MinMaxScaler()
    scaler.fit(data)
    
    print('Saving scaler to: ', scaler_output_path)
    joblib.dump(scaler, scaler_output_path)
    
    print('---Transforming data---')
    t_data = scaler.transform(data)
    print('---Transforming complete ----')
    
    
    
    print('Saving transformed training data to {}'.format(output_path))
    pd.DataFrame(t_data).to_csv(output_path, header=False, index=False)
