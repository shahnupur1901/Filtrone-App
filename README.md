# Filtrone-App

This is an image classification model for a fashion dataset with new deep learning models as well as with pretrained models with transfer learning. These models provide filters on : Gender, Subcategory, Article type and color.

Model Workflow :
1. After user authentication, user is redirected to the app's main page where the image can be uploaded. 
![Filtrone1](https://user-images.githubusercontent.com/67814929/144272905-f5ebfd86-5914-449e-b33d-6168f4334232.png)

2. The deep learning models is used to predict the filters in the backend, and the resultant filters are printed here.
![Filtrone2](https://user-images.githubusercontent.com/67814929/144272922-8c30dedc-2487-4f54-a534-2f18dfc92f27.png)

3. Feedback page to record user satisfaction.
![Filtrone3](https://user-images.githubusercontent.com/67814929/144272936-9446ec20-7f94-483e-8a38-2e22ed35069a.png)

4. Final page.
![Filtrone 4](https://user-images.githubusercontent.com/67814929/144272947-a81886c8-c402-4974-bc38-65bbf9c0cbcc.png)

__________________________________________________________________________________________________________________________________________________________________

Filters :
1. Sub-categories : 23 categories including - “Topwear" "Bags" "Belts" "Bottomwear" "Dress" "Eyewear" "Flip Flops" "Fragrance" "Free Gifts" "Headwear" "Innerwear" "Jewellery", "Loungewear and Nightwear" "Mufflers" "Sandal" "Saree" "Shoes""Socks""Ties" "Topwear" "Wallets" "Watches"

2. Article Type : 67 categories including - Jeans', 'Watches', 'Track Pants', 'Socks', 'Casual Shoes','Belts', 'Flip Flops', 'Handbags', 'Sandals', 'Shoe Accessories', 'Deodorant', 'Formal Shoes', 'Bracelet','Flats', 'Kurtas', 'Sports Shoes', 'Shorts', 'Briefs', 'Sarees', 'Heels', 'Sunglasses', 'Innerwear Vests','Pendant', 'Laptop Bag', 'Night suits', 'Skirts', 'Ring','Kurta Sets', 'Clutches', 'Backpacks', etc.

3. Gender : Women, Men, Girl, Boy, Unisex
__________________________________________________________________________________________________________________________________________________________________

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
