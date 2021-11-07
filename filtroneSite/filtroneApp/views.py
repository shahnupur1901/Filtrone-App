from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from colorthief import ColorThief
import webcolors as wc
import cv2
from PIL import Image
# Create your views here.
from tensorflow import keras 
import json
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from tensorflow import Graph

#Input Image specifications
img_height, img_width = 96, 96


#Labels for classes
with open('/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/genderClasses.json') as json_file: 
    genderLabelInfo = json.load(json_file)
    genderLabelInfo = dict((v,k) for k,v in genderLabelInfo.items())

with open('/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/subCategoryClasses.json') as json_file:
    subCategoryLabelInfo = json.load(json_file)
    subCategoryLabelInfo = dict((v,k) for k,v in subCategoryLabelInfo.items())

with open('/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/usageClasses.json') as json_file:
    usageLabelInfo = json.load(json_file)
    usageLabelInfo = dict((v,k) for k,v in usageLabelInfo.items())

with open('/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/modelfortopweararticletype.json') as json_file:
    topwearLabelInfo = json.load(json_file)
    topwearLabelInfo = dict((v,k) for k,v in topwearLabelInfo.items())

with open('/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/articleTypes.json') as json_file:
    articleTypeLabelInfo = json.load(json_file)
    articleTypeLabelInfo = dict((v,k) for k,v in articleTypeLabelInfo.items())

#Generating deep learning model sessions with Graph
genderModel_Graph = Graph()
with genderModel_Graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        genderModel = load_model("/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/modelForGender.h5")

subCategoryModel_Graph = Graph()
with subCategoryModel_Graph.as_default():
    tf_session2 = tf.compat.v1.Session()
    with tf_session2.as_default():
        subCategoryModel = load_model("/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/modelForSubcategory.h5")

usageModel_Graph = Graph()
with usageModel_Graph.as_default():
    tf_session3 = tf.compat.v1.Session()
    with tf_session3.as_default():
        usageModel = load_model("/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/modelForUsage.h5")

topwearModel_Graph = Graph()
with topwearModel_Graph.as_default():
    tf_session4 = tf.compat.v1.Session()
    with tf_session4.as_default():
        topwearModel = load_model("/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/modelForTopArticleType85.h5")

articleTypeModel_Graph = Graph()
with articleTypeModel_Graph.as_default():
    tf_session5 = tf.compat.v1.Session()
    with tf_session5.as_default():
        articleTypeModel = load_model("/home/nupur/MyntraHackathon/deployModel/filtroneSite/Model/modelForArticleType82.h5")


#After redirection from Authentication
def index(request):
    return render(request,'index.html')

#After submitting image
def submitImage(request):
    FileObject = request.FILES["filename"]
    fs = FileSystemStorage()
    fileName = fs.save(FileObject.name,FileObject)
    fileName = fs.url(fileName)
    testImage = "." + fileName
    #Image processing
    img = image.load_img(testImage,target_size=(img_height,img_width))
    color = getProductColor(testImage)
    x = image.img_to_array(img)
    x = x/255
    x = x.reshape(1,img_height,img_width,3)
    #Model Prediction
    with genderModel_Graph.as_default():
        with tf_session.as_default():
            predicted = genderModel.predict(x)
    predictedGenderlabel = genderLabelInfo[np.argmax(predicted)]

    with subCategoryModel_Graph.as_default():
        with tf_session2.as_default():
            predicted = subCategoryModel.predict(x)
            print(predicted)
    predictedsubCategorylabel = subCategoryLabelInfo[np.argmax(predicted)]

    if(predictedsubCategorylabel=="Topwear"):
        with topwearModel_Graph.as_default():
            with tf_session4.as_default():
                predicted = topwearModel.predict(x)
                predictedwearlabel = topwearLabelInfo[np.argmax(predicted)]
    else:
        with articleTypeModel_Graph.as_default():
            with tf_session5.as_default():
                predicted = articleTypeModel.predict(x)
                predictedwearlabel = articleTypeLabelInfo[np.argmax(predicted)]



    with usageModel_Graph.as_default():
        with tf_session3.as_default():
            predicted = usageModel.predict(x)
    predictedusagelabel = usageLabelInfo[np.argmax(predicted)]
    if(predictedusagelabel!="Sports"):
        predictedusagelabel = ""


    return render(request,'label.html',{'fileName':fileName, "Gender" : predictedGenderlabel, "SubCategory":predictedsubCategorylabel,
    "Usage":predictedusagelabel, "ArticleType":predictedwearlabel, "Color":color.capitalize()})

#After feedback submission
def submit(request) :
    ms = ["Yes", "No"]
    if request.method=="POST":
        clickedOption = request.POST.getlist('clickedOption')
        print(clickedOption)
        if clickedOption==["Yes"]:
            message = "We are glad to hear that! Thank you for your valuable feedback."
        else :
            message = "We are sorry to hear that. Thank you for your valuable feedback."
    return render(request,"serverMessage.html",{"message":message})

#Feedback submission
def submitFeedback(request):
    return render(request,"checkbox.html")

##Obtaining dominant color of image function
def getProductColor(imgpath) :
    im = Image.open(imgpath)
    width, height = im.size
    left = width/4
    top = height / 4
    right = 3 * width/ 4
    bottom = 3 * height/ 4
 
# Cropped image of above dimension
# (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    fp = "/home/nupur/MyntraHackathon/deployModel/filtroneSite/media/cropped.png"
    im1.save(fp)
    color_thief = ColorThief(fp)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    # build a color palette
    imghex = wc.rgb_to_hex(dominant_color)
    def get_approx_color(hex_color):
        orig = wc.hex_to_rgb(hex_color)
        similarity = {}
        for hex_code, color_name in wc.css3_hex_to_names.items():
            approx = wc.hex_to_rgb(hex_code)
            similarity[color_name] = sum(np.subtract(orig, approx) ** 2)
        return min(similarity, key=similarity.get)

    def get_color_name(hex_color):
        try:
            return wc.hex_to_name(hex_color)
        except ValueError:
            return get_approx_color(hex_color)
    return get_color_name(imghex)