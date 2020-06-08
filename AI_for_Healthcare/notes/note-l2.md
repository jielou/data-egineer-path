---
noteId: "5a98b310a98611ea9a2347eb31c960da"
tags: []

---

# 2D Medical Imaging Exploratory Data Analysis

## Resources

[DICOM key concepts](https://www.dicomstandard.org/concepts/)
## Key takeaways
### DICOM Standard

DICOM is short for “Digital Imaging and Communications in Medicine”, which is the standard for the communication and management of medical imaging information and related data. It was developed by the American College of Radiologists in 1993 to allow for interoperability.

DICOM ensures the "interoperability" of medical imaging systems by making it easier to perform the following actions on medical images:
Produce, Store, Display, Send, Query, Process, Retrieve, Print
By using DICOM, one can get derived structured documents and manage the related workflow more conveniently.

DICOM files are a medical imaging file that is in the format that conforms to the DICOM standard.

A DICOM file contains information about the imaging acquisition method, the actual medical images, and patient information. It has a header component that contains information about the acquired image and an image component that is a set of pixel data representing the actual images

Protected Health Information (PHI) is part of DICOM and clinical data and radiologist report are not part of DICOM.

With 2D imaging, a single 2D image is known as a single DICOM series. All image series combined comprise a study of the patient, known as a DICOM study.

### read dicom info in Python
The pydicom package allows us to extract all of the metadata from a set of DICOM files and store them in a way that is easy to access.

`my_dicom = pydicom.dcmread(“MY_DICOM.dcm”)` is used to read a DICOM file.

`my_dicom_image = my_dicom.pixel_array` is used to access the actual pixel data of the image.

`matplotlib.pyplot.imshow(my_dicom_image, cmap = ‘gray’)` is used to show the image.

It is worth noting that the data returned in my_dicom.pixel_array will be in the coordinate format [y,x].

### Edge case

Not all 2D medical images are stored as a DICOM. Microscopy images are not stored in DICOM since they do not come from a digital machine. Instead, they are biological data and come from smeared physical cells from patients.

The first step of transforming microscopy into a digital image is to get the cell sample from a patient. Then cells are dyed into different colors based on their structure and viewed by a microscope. The microscopy data is then captured by a camera to form a digital image. This transformation technique is called digital pathology.

Once images are digitized, they can be processed with ML in the same way as you would with the pixel data extracted from DICOM.
