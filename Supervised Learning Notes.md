# Identifying class based on text

Assigning correct class label to given input

1. Topic identification
2. Spam Detection
3. Sentiment Analysis
4. Spelling Correction

Classification model on properties (features) and their importance (Weights) from labelled instances

X : Set of attributes or features {x1, x2,...xn}
y: 'class' label from the label set Y = {y1, y2, ... yn}

## Supervised Classification

Training Phase -Labeled
a. Training dataset
b. Validation dataset

Lookouts:

* What are the features ? How do you represent them ?

Feature Identification:
1. How do you handle commonly occurring Words / Stop words
2. Normalization: Make all lower case vs leave as-is
3. Stemming / Lemmatization
4. Characteristics of words - Capitalization
5. Parts of Speech 
6. Grammatical Structure, Sentence Structure
7. Grouping words - with similar meanings Eg: {buy, purchase} {Mr./Ms., Number/Digits, Dates}
8. Based on word sequences - Bi-grams, tri-grams, n-grams: "White House"
9. Character sub-sequencing - "ing", "ion"

* What is the classification model/algorithm ?
* What are the model parameters ?

Inference Phase - Unlabeled
Test dataset

Lookouts:

* What is the expected performance ? What is a good measure ?

## Classification paradigms

1. Binary Classification
2. Multi-class classification
3. Multi-label classification
