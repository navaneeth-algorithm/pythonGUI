# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:36:17 2019

@author: hp
"""
import sys
from PyQt5.QtWidgets import  QMainWindow,QLabel,QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        label = QLabel("Label is here")
        self.resize(20,20)
        label.show()
        




app = QApplication([])
    
sys.exit(app.exec_())
        