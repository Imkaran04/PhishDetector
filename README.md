# PhishDetector
 
Phishing Domain Detection
Phishing Domain Detection is a machine learning project that aims to classify domain names as either legitimate or phishing. The project utilizes the Random Forest Classifier algorithm to train a model on a dataset of domain names labeled as legitimate or phishing. The resulting model can then be used to predict whether a given domain name is legitimate or phishing based on its features.

Getting Started
To use the project, you will need to install Python and some required libraries such as scikit-learn, pandas, numpy, and matplotlib. Once you have these installed, you can clone the repository and run the main script phishing_detection.py. This script loads the dataset, preprocesses the data, trains the model, and evaluates its performance.

Dataset
The dataset used in this project contains 10,000 domain names, half of which are legitimate and half of which are phishing. The features used to represent each domain name are length, number of digits, number of hyphens, and number of subdomains.

Preprocessing
Before training the model, the dataset is preprocessed by encoding the target variable (legitimate or phishing) as a binary variable and scaling the features using the StandardScaler function from scikit-learn. The preprocessed dataset is then split into training and testing sets using a 80:20 split.

Training and Evaluation
The model is trained using the Random Forest Classifier algorithm with hyperparameters tuned using the Validation Curve function from Yellowbrick. The performance of the model is evaluated using accuracy score, precision score, recall score, and F1 score.

Conclusion
Phishing Domain Detection is a machine learning project that demonstrates the use of the Random Forest Classifier algorithm in detecting phishing domain names. The project provides a model that can be used to predict whether a given domain name is legitimate or phishing with high accuracy. The project can be further extended by adding more features and experimenting with other machine learning algorithms.




