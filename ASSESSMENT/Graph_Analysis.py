# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 01:05:03 2022

@author: home
"""
from Import_Modules import *

from DecisionTree import Tree
import seaborn as sns


from Import_Modules import *

from tkinter import * 
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import NW, Canvas, PhotoImage, filedialog
#from PIL import Image, ImageTk


#Class Analysis for graph visualization
class Analysis:
   
    def __init__(self):
        
        Tree.__init__(self)
        
        
        #Pie graph  Visualization using plt 
        self.target_counts=self.dataset['Result'].value_counts().values
        self.gender_counts=self.dataset['Gender'].value_counts().values
    
        fig1, axes=plt.subplots(nrows=1, ncols=2,figsize=(10,25))
    
        plt.title('Liver patients Analysis', fontsize=15)
        
        self.target_sizes= self.dataset.groupby('Result').size()
        
        axes[0].pie(x=self.target_counts,
                    labels=['patient({})'.format(self.target_sizes[1]),'not patient({})'.format(self.target_sizes[2])],
                    autopct='%1.1f%%')
        axes[0].set_title("Percentage of liver patient")
    
        self.gender_sizes = self.dataset.groupby('Gender').size()
        
        axes[1].pie(x=self.gender_counts, 
        labels=['male({})'.format(self.gender_sizes['Male']), 'female({})'.format(self.gender_sizes['Female'])], 
        autopct="%1.1f%%")
        axes[1].set_title("Age wise liver patient")
        
        
       
        
# if __name__ == "__main__":
#     graph = Analysis()
#     graph.plot_graphs()       