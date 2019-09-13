# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:38:25 2019

@author: Sefa3
"""

import sys

from PyQt5 import QtWidgets, QtGui

def Pencere():
    # uygulama objesi oluşturmak için;
    app = QtWidgets.QApplication(sys.argv)
    
    # pencere oluşturmak için;
    pencere = QtWidgets.QWidget()
    
    # başlık oluşturmak için;
    pencere.setWindowTitle("PyQt5 Ders 2")
    
    # pencerenin üzerine yazı eklemek için;
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Burası bir yazıdır.")
    
    # etiketi pencerenin içerisinde taşımak için;
    etiket1.move(200, 30)
    
    # pencerenin içerisine resim eklemek için;
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("Atatürk.jpg"))
    etiket2.move(0, 50)
    
    # pencerenin büyüklüğünü belirlemek için(opsiyonel);
    pencere.setGeometry(100, 100, 500, 500)
    
    # pencereyi göstermek için;
    pencere.show()
    
    # çarpıya basmadığımız sürece uygulamayı çalıştırması için;
    sys.exit(app.exec_())
    
Pencere()