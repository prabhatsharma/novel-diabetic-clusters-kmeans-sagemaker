# Novel Diabetic cluster identification using sagemaker

Based on the paper [Novel subgroups of adult-onset diabetes and their association with outcomes: a data-driven cluster analysis of six variables](
https://www.thelancet.com/journals/landia/article/PIIS2213-8587(18)30051-2/fulltext), we use sagemaker to cluster the data based on the following variables:

1. glutamate decarboxylase antibodies (GAD), 
2. age at diagnosis, 
3. BMI
4. HbA1c
5. [homoeostatic model assessment](https://en.wikipedia.org/wiki/Homeostatic_model_assessment) estimates of insulin resistance
6. [homoeostatic model assessment](https://en.wikipedia.org/wiki/Homeostatic_model_assessment) estimates of β-cell function


This will allow us to place the patients in 5 finely defined clusters as opposed to generic 2 clusters (Type 1 and Type 2). This will allow healthcare providers to provide more targetted care to patients.

# Architecture diagram

![Architecture diagram](diabetes.png)

