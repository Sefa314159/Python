# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:56:01 2019

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
    
    # buton oluşturmak için;
    buton = QtWidgets.QPushButton(pencere)
    
    # butona isim vermek için;
    buton.setText("Burası bir butondur.")
    
    # etiket oluşturmak için;
    etiket = QtWidgets.QLabel(pencere)
    
    # etikete isim vermek için;
    etiket.setText("Merhaba Dünya")
    
    etiket.move(200, 80)
    
    # pencereyi göstermek için;
    pencere.show()
    
    # çarpıya basmadığımız sürece uygulamayı çalıştırması için;
    sys.exit(app.exec_())
    
Pencere()