
# Classifier - function of input data

Decision Boundaries:

* Class A and Class B
* How do you find decision boundaries
    1. Training data - Red +/-
    2, test data - Black +/-

    If training data and test data is different - it is an issue of "Over Fitting"

1. Linear Boundaries
   a. Easy to find
   b. Easy to evaluate
   c. More generalizable: "Occam's razor"

   How to find Linear Boundary - Through slope (w)
   Methods: Perceptron, Linear Discriminative Analysis, Linear least squares, SVM

   Problem: If linearly separable boundaries will be infinite

Support Vector Machines are Maximum-margin classifiers

* SVM's are linear classifiers that find a hyperplane to separate two classes of data: positive and negative

SVM : Multi-class classification:

* One vs Rest
* One vs One

SVM Parameters (I) : Parameters C

* Regularization - How much importance need to be given to individual data point compared to better generalized model
* Regularization C
  * Larger value of C = less regularization
        * Fit training data as well as possible, every data point important
  * Smaller value of C = more regularization
        * More tolerant to errors on individual data points

* Other Params:
  Linear Kernels work best for text data
  * Other Kernels include rbf, polynomial

* Multi_class: ovr (one-vs-rest)
* class_weight: Different classes can get different weights

Model selection:
Cross-validation

Scikit-learn : test_size = 0.333
