# Filtrone-App
![Filtrone1](https://user-images.githubusercontent.com/67814929/144270717-00e276f5-9294-47eb-9360-16b5a06469c6.png)
![Filtrone2](https://user-images.githubusercontent.com/67814929/144271023-e14dfbe6-a8fe-48ca-91b3-1bf3eb707c16.png)
![Filtrone3](https://user-images.githubusercontent.com/67814929/144271040-a3cb9c5c-c82c-4599-ac9b-ec1b59c4123e.png)
![Filtrone 4](https://user-images.githubusercontent.com/67814929/144271062-9162f43f-2556-4e9b-9aac-03e90350c0f9.png)
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
