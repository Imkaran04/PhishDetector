# PhishDetector

 
Phishing Domain Detection

Phishing Domain Detection is a machine learning project that aims to classify domain names as either legitimate or phishing. The project utilizes the Random Forest Classifier algorithm to train a model on a dataset of domain names labeled as legitimate or phishing. The resulting model can then be used to predict whether a given domain name is legitimate or phishing based on its features.

Getting Started

Project Overview
Phishing Domain Detection is designed to run locally on your computer, eliminating the need for cloud-based processing and keeping sensitive data secure. The project includes several key components, including a Low-Level Design (LLD) document, a High-Level Design (HLD) document, a Detailed Project Report (DPR), a wireframe document, and a LinkedIn post.

The LLD document provides a detailed technical specification for the project, including the architecture, data flow, algorithms, and technology stack. The HLD document provides a higher-level overview of the project, including the user interface, hardware and software interfaces, performance requirements, and non-functional attributes.

The DPR provides an in-depth analysis of the project, including the problem statement, objectives, methodology, results, and conclusion. The wireframe document includes the visual representation of the user interface and flow of the application. The LinkedIn post is a social media promotion of the project that highlights the key features and benefits.

Project Architecture
The project uses advanced machine learning algorithms and natural language processing techniques to analyze URLs in real-time and detect potential phishing attacks. The architecture includes multiple modules, including URL extraction, feature extraction, model training, and prediction. The project also includes customizable settings for adjusting the sensitivity and specificity of the detection.

For a detailed technical specification and design overview of the project, please refer to the LLD and HLD documents in the repository.

Dataset

The dataset used in this project contains 10,000 domain names, half of which are legitimate and half of which are phishing. The features used to represent each domain name are length, number of digits, number of hyphens, and number of subdomains.

Preprocessing

Before training the model, the dataset is preprocessed by encoding the target variable (legitimate or phishing) as a binary variable and scaling the features using the StandardScaler function from scikit-learn. The preprocessed dataset is then split into training and testing sets using a 80:20 split.

Training and Evaluation

The model is trained using the Random Forest Classifier algorithm with hyperparameters tuned using the Validation Curve function from Yellowbrick. The performance of the model is evaluated using accuracy score, precision score, recall score, and F1 score.


Video Demonstration
We have provided a video demonstration of the Phishing Domain Detection project in action. 

Wireframe Document
We have provided a wireframe document that includes the visual representation of the user interface and flow of the application.

LinkedIn Promotion
We have also posted a LinkedIn promotion to highlight the key features and benefits of the Phishing Domain Detection project. 


Please Refer the below links to navigate to the different documents:

[Link to DPR Document] [https://github.com/Imkaran04/PhishDetector/blob/main/Documents/DPR%20Phishing%20Domain%20Detection.pdf]

[Link to HLD Document] [https://github.com/Imkaran04/PhishDetector/blob/main/Documents/HLD%20Phishing%20Domain%20Detection.pdf]

[Link to LLD Document] [https://github.com/Imkaran04/PhishDetector/blob/main/Documents/LLD%20Phishing%20Domain%20Detection.pdf]

[Link to Architecture Document] [https://github.com/Imkaran04/PhishDetector/blob/main/Documents/Architecture%20Phishing%20Domain%20Detection.pdf]

[Link to Wireframe Document] [https://github.com/Imkaran04/PhishDetector/blob/main/Documents/Wireframe%20Phishing%20Domain%20Detection.pdf]


Other Links:

Link to LinkedIn Post [url]

Link to Demo Video [url]









Conclusion
The Phishing Domain Detection project is a powerful tool for detecting and preventing phishing attacks in real-time. With its advanced machine learning algorithms and natural language processing techniques, it can analyze URLs and predict potential phishing attacks with high accuracy. The project is designed to run locally on your computer, eliminating the need for cloud-based processing and keeping sensitive data secure. We hope you find this project useful and look forward to your feedback.










