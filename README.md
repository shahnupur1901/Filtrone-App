# Filtrone-App

Video Demonstration :https://drive.google.com/drive/folders/1OFHx5us2bGQDYpoJvmoO8qBveIiWOpeF
To check out the examples of the outputs of the model : go to FiltroneExamples.pdf
For information about the models : go to Model Information.pdf

Tech Stack :
For the deep learning models : 
Python libraries including tensorflow, scikit-learn, keras
For the web framework :
Django

Github code guide :
The Deep Learning Models are in the DeepLearningModels folder with the Google Colab files attached.
The Django code is in the filtroneSite.
FiltroneSite navigation:
1. FiltroneApp
Views.py in FiltroneApp contains the functions for each action.
The static folder conains the CSS files.
2. Model
Contains the stored models in the h5 format and the json files for the labels.
3. Templates
Contains the HTML codes.
4. The subfile FiltroneSite in FIltroneSite has settings.py and urls.py which have been configured for the app.

Dataset : https://www.kaggle.com/paramaggarwal/fashion-product-images-small
