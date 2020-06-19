# Hands on Machine Learning with Scikit Learn and Tensorflow

## Chapter 2

### train_test_split

use each instance's identifier to decide whether or not it should go in the test set (assuming instances have a unique and immutable identifier). For example, you could compute a hash of each instance's identifier, keep only the last byte of the bash and put the instance in the test set if this value is lower or equal to 51 (~20% of 256). This ensures that the test set will remain consistent across multiple runs, even if you refresh the dataset.


## Chapter 3

### precision-recal vs ROC

As a rule of thumb, you should prefer the PR curve whenever the positive class is rare or when you care more about the false positives than the false negatives. Otherwise, ROC curve is preferred. 

### multiclass classification

- one-versus-all: train n binary classifiers and then get the decision score from each classifier for the record, and select the class whose outputs the highest score.
- one-versus-one: train a binary classifier for every pair of digits. For N classes, you need to train Nx(N-1)/2 classifiers. 
- in scikit-learn, it automaticcally runs OvA, except for SVM classifiers for which it uses OvO because it scales porrly with the size of teh training set. 

### multilabel classification
outputs multiple binary labels

###
multilabel classification where each label can be multiclass
