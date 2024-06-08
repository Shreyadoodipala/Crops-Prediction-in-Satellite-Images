# Crops-Prediction-in-Satellite-Images
Prediction of Crops in multispectral images using CNNs 
<p>
  Dataset: SICKLE- <a href="https://sites.google.com/iiitd.ac.in/sickle/">https://sites.google.com/iiitd.ac.in/sickle/</a> <br>
  Landsat-8 (L8) images from the SICKLE toy dataset were used.
</p>

## Preprocessing
The images are in the form of multiple .npz files in folders. They were analyzed, and the Landsat-8 images have 19 channels, and are mostly of size (12,12) with some variations. <br>
Images of size (11,12) or (12,11) are padded with 0s, while the rest are not considered. <br>
Run the dataset_create.py file in the npy folder.

## CNN Architecture
![image](https://github.com/Shreyadoodipala/Crops-Prediction-in-Satellite-Images/assets/95224610/7de5b858-67fb-4295-bed5-7d6d2ee85349)

<p>The testing.ipynb file can be used to check the prediction for a single image. </p>
