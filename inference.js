var AWS = require('aws-sdk')

AWS.config.update({ region: 'us-east-2' });

var sagemakerruntime = new AWS.SageMakerRuntime();

var inference_data = [758, 64, 36, 2.83, 50.28] // GAD, AGE, BMI, HOMA_IR, HOMA_Beta 


// Data for normalizing
var mean = [498.907, 50.0303, 29.4696, 2.289492000000002, 74.49937000000021] // mean of source data
var std = [289.87433115711855, 28.657887384818498, 11.498821597442676, 1.306044393246921, 526.7579254124425] // standard deviation of source data

// Normalize data
var consumable_data = inference_data.map((value, index) => {
    return (value - mean[index]) / std[index] // normalize data
})


// Invoke sagemaker endpoint for prediction
var params = {
    Body: consumable_data.toString(),
    EndpointName: 'kmeans-2020-05-16-03-23-14-106',
    ContentType: 'text/csv',
  };

sagemakerruntime.invokeEndpoint(params, function (err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(JSON.parse(data.Body.toString()));           // successful response
});