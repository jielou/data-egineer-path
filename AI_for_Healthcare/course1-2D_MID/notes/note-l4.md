---
noteId: "898f64a1ab5411eaa655bf1f234e3db2"
tags: []

---


# classifiction Models for 2D Medical Imaging

## resources

[Otsu'e mthod](https://medium.com/@hbyacademic/otsu-thresholding-4337710dc519)
[keras documentation](https://keras.io/api/preprocessing/image/)
[a fastai course](https://course.fast.ai/)

## key takeaways

### difference between models

#### ML vs. DL
The biggest difference between ML and DL is the concept of feature selection. Classical machine learning algorithms require predefined features in images. And, it takes up a lot of time and effort to design features. When deep learning came along, it was so groundbreaking because it worked to discover important features, taking this burden off of the algorithm researchers.

#### Ostu's method
It’s often used for background extraction and classification. It takes the intensity distribution of an image and searches it to find the intensity threshold that minimizes the variance in each of the two classes. Once it discovers that threshold, it considers every pixel on one side of that image to be one class and on the other side to be another class.

#### Convolutional neural network (CNN)
There are several sets of convolutional layers in a CNN model. Each layer is made up of a set of filters that are looking for features. Layers that come early in a CNN model look for very simple features such as directional lines and layers that come later look for complex features such as shapes.

Note that the input image size must match the size of the first set of convolutional layers.

#### U-Net
U-Net is used for segmentation problems and it is more commonly used in 3D medical imaging. It's important to note that a limitation of 2D imaging is the inability to measure the volume of structures. 2D medical imaging only measures the area with respect to the angle of the image taken, which limits its utility in segmenting the whole area.

### Gold standard
The gold standard for a particular type of data refers to the method that detects disease with the highest sensitivity and accuracy. Any new method that is developed can be compared to this to determine its performance. The gold standard is different for different diseases.

- for pneumonia, gold standard is a biospy. (take very long time)
- for mamagraphy screening, the gold standard is a radiologists read. if mass found, a biospy is the gold standard to tell if it is begign or malignant. Radiologists reports are not with DICOMs, and need extraction of diagnosis. Biospy is outside PACS. 


#### Ground truth
Often times, the gold standard is unattainable for an algorithm developer. So, you still need to establish the ground truth to compare your algorithm.

Ground truths can be created in many different ways. Typical sources of ground truth are

#### Biopsy-based labeling. Limitations: difficult and expensive to obtain.
NLP extraction. Limitations: may not be accurate.
Expert (radiologist) labeling. Limitations: expensive and requires a lot of time to come up with labeling protocols.
Labeling by another state-of-the-art algorithm. Limitations: may not be accurate.
#### Silver standard
The silver standard involves hiring several radiologists to each make their own diagnosis of an image. The final diagnosis is then determined by a voting system across all of the radiologists’ labels for each image. Note, sometimes radiologists’ experience levels are taken into account and votes are weighted by years of experience.

### Image Pre-Processing

Goals:
- remove potential noise from your images (e.g. background extraction)
    - like otsu's method
- Enforce some normalizationi across images (zero-mean, standardization)
    - deep learning prefers standardization
- Enlarge your dataset (image augmentation)
- Resize for your CNN architecture's required input

**note**
- vertical_flip augementation is not approriate for medical image
- validation data should bever be augmented

#### intensity normalization
Intensity normalization is good practice and should always be done prior to using data for training. Making all of your intensity values fall within a small range that is close to zero helps the weights on our convolutional filters stay under control

There are two types of normalization that you can perform.

- zero-meaning: subtract that mean intensity value from every pixel.
- standardization: subtract the mean from each pixel and divide by the image’s standard deviation.

#### Image augmentation
Image augmentation allows us to create different versions of the original data. Keras provides ImageDataGenerator package for image augmentation.

Note: not all image augmentation method is appropriate for medical imaging. A vertical flip should never be applied. And validation data should NEVER be augmented.

#### Image resize
CNNs have an input layer that specifies the size of the image they can process. Keras flow_from_directory have a target_size parameter to resize image.

### fine-tuning CNNs
The first several layers of filters trained are only going to learn line- and shape-based features because their visual fields are so small. We can reuse or freeze the pre-trained weights of the first few layers and only need to train filter weights to detect higher-order features that are more relevant to your specific use cases. We call this process that only makes adjustment of weights in the last a few layers fine-tuning.

One of the key pieces of fine-tuning is the last layer. We need to adjust the dimension of the last layer to match our specific use cases. We can also add new layers to train from scratch.