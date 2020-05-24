import boto3
import numpy as np
import json


client = boto3.client('sagemaker-runtime')

mean =  np.array([498.907, 50.0303, 29.4696, 2.289492000000002, 74.49937000000021])
std =  np.array([289.87433115711855, 28.657887384818498, 11.498821597442676, 1.306044393246921, 526.7579254124425])

inference_data = [758,64,36,2.83,50.28]

# numpy array to bytes
test_a1 = np.array(inference_data).reshape(1,5)
test_a1 = (inference_data - mean)/std
test_a1 = np.float32(test_a1)
test_a1 = test_a1.tolist()
test_a1 = ",".join(map(str, test_a1))

print(test_a1)

d1 = '0.89381146,  0.4874644,   0.5679191,   0.41385117, -0.04597818'


response = client.invoke_endpoint(
    EndpointName='kmeans-2020-05-16-03-23-14-106',
    Body = test_a1,
    ContentType='text/csv',
)

result = json.loads(response['Body'].read().decode())

print(result)



