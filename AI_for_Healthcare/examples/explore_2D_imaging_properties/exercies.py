import pydicom
import numpy as np

#read dcm
dcm = pydicom.dcmread('dicom_00023075_033.dcm')

#show images
plt.imshow(dcm.pixel_array,cmap='gray')

# normalize images
mean_intensity = np.mean(dcm.pixel_array)
mean_intensity
std_intensity = np.std(dcm.pixel_array)
std_intensity
new_img = dcm.pixel_array.copy()
new_img = (new_img - mean_intensity)/std_intensity

##extract headers into a dataframe
dcm.Modality
dcm.StudyDescription
dcm.PatientID
dcm.PatientSex
dcm.PatientAge