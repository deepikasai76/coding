
# Importing the required packages
import numpy as np
import pandas as pd
import sys, os
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import tree
import pymongo 
from pymongo import MongoClient 
import urllib.parse
from urllib.parse import quote_plus

#Parsing the password to encode into ASCII code, so that server can take the password to give accesss to the user
#Connecting with the MongoDB Atlas with user and password
username = urllib.parse.quote("SaideepikaKandiganti")
password = urllib.parse.quote("Deepika@123")
client = pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.ztqqclq.mongodb.net/?retryWrites=true&w=majority" %(username, password))
mydb = client['MyMongo']
mycol = mydb['MyCollec']
#print(mydb)

# Function importing Dataset
class Tree:
    def __init__(self):
        
        
        self.dataset = pd.read_csv('indian_liver_patient.csv',
        sep= ',', low_memory=True)
        
        self.dataset.rename(columns={'Dataset':'Result'}, inplace=True)
        self.dataset.info()
    
        self.dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

        self.dataset.fillna(999, inplace=True)
        self.length = len(self.dataset)
        self.shape = self.dataset.shape
        # Printing the dataswet shape
        return None
        

    # Function to split the dataset
    def splitting_dataset(self):
    
        # from sklearn.preprocessing import LabelEncoder
        # dataset = dataset.apply(LabelEncoder().fit_transform)
        # print("dtree", dataset.head())
        
        self.dataset['Gender'] = self.dataset['Gender'].map({'Male': 1, 'Female': 2})
        
        # Dropping the missing values
        self.dataset.dropna()
            
        self.X = self.dataset.drop("Result", axis=1)
        print("X data: ", self.X)
        self.Y = self.dataset["Result"]
        print("Y data: ", self.Y)
        #convert y values to categori
        # Splitting the dataset into train and test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split( 
        self.X, self.Y, random_state = 100)

        return self.X, self.Y, self.X_train, self.X_test, self.y_train, self.y_test

    # Function to perform training with giniIndex.
    def get_split(self):
        
        self.X = self.dataset.drop("Result", axis=1)
        print("X data: ", self.X)
        self.Y = self.dataset["Result"]
        print("Y data: ", self.Y)
        
        return self.X,  self.Y
    
    
    
    def get_gini(self, *args, **kwargs):
        
        #getattr(self.X_train, self.X_test, self.y_train)
        # Creating the classifier object
        self.classifier = DecisionTreeClassifier(criterion = "gini",random_state =5,max_depth=4)

        # Performing training
        self.classifier.fit(self.X_train,self. y_train)
        """Plot the tree and save to file."""
        
        fig, axe = plt.subplots(figsize=(10,10))#dpi=200
        
        tree.plot_tree(self.classifier, ax = axe, filled=True, rounded=True, fontsize=7, max_depth=4)
        
        plt.savefig(f'Final_DecisionTree.png')
        
        plt.show()
         
        self.text_representation = tree.export_text(self.classifier)
        #print(self.text_representation)
        
        #plt.savefig(f'Final_DecisionTree.png')
        
        
        #plt.imsave('Final_DecisionTree.png', Decision Tree)
        
        return self.classifier
    
   

    # Function to make get_get_predictionsss
    def get_predictions(self,clf_object):
        
        self.clf_object = clf_object
        
        # Predicton on test with giniIndex
        self.y_pred = clf_object.predict(self.X_test)
        print("Predicted values:")
        print(self.y_pred)
        return self.y_pred

    # Function to calculate accuracy
    def accuracy(self,y_pred, y_test):

        print("Confusion Matrix: ",
            confusion_matrix(self.y_test, self.y_pred))

        print ("Accuracy : ",
        accuracy_score(self.y_test,self.y_pred)*100)
        
        
    
   
    # Driver code
if __name__== '__main__':

        # Building Phase
        data = Tree()
        X, Y, X_train, X_test, y_train, y_test = data.splitting_dataset()
        data.classifier = data.get_gini(X_train,y_train)
        
        print("Train Accuracy : ", metrics.accuracy_score(y_train, data.classifier.predict(X_train)))
        print("Test Accuracy : ", metrics.accuracy_score(y_test, data.classifier.predict(X_test)))

    #   clf_entropy = tarin_using_entropy(X_train, X_test, y_train)

        # Operational Phase
        print("Gini Index calculations:")

        # get_predictions using gini
        y_pred_gini = data.get_predictions(data.classifier)
        
        data.accuracy(y_test, y_pred_gini)
       