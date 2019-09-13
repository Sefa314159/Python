# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:29:41 2019

@author: Sefa3
"""

import sys

from PyQt5 import QtWidgets

def Pencere():
    # uygulama objesi oluşturmak için;
    app = QtWidgets.QApplication(sys.argv)
    
    # pencere oluşturmak için;
    pencere = QtWidgets.QWidget()
    
    # başlık oluşturmak için;
    pencere.setWindowTitle("PyQt5 Ders 1")
    
    # pencerenin büyüklüğünü belirlemek için(opsiyonel);
    pencere.setGeometry(100, 100, 500, 500)
    
    # pencereyi göstermek için;
    pencere.show()
    
    # çarpıya basmadığımız sürece uygulamayı çalıştırması için;
    sys.exit(app.exec_())
    
Pencere()
