# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:26:01 2019

@author: Sefa3
"""

import sys

from PyQt5 import QtWidgets

def Pencere():
    # uygulama objesi oluşturmak için;
    app = QtWidgets.QApplication(sys.argv)
    
    # okay adında buton oluşturmak için;
    okay = QtWidgets.QPushButton("Tamam")
    
    # cancel adında buton oluşturmak için;
    cancel = QtWidgets.QPushButton("İptal")
    
    # horizontal box oluşturmak için;
    h_box = QtWidgets.QHBoxLayout()
    
    # boxlarımızı sağ tarafa sabitliyebilmek için;
    h_box.addStretch() # aslında boşluk bırakıyor.
    
    # horizontal box layout'unun içerisine okay ve cancel'ı eklemek için;
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    
    # boxlarımızı sol tarafa sabitliyebilmek için;
    # h_box.addStretch()
    
    # aynısını vertical box ile yapmak için;
    # v_box = QtWidgets.QVBoxLayout()
    # v_box.addStretch()
    # v_box.addWidget(okay)
    # v_box.addWidget(cancel)
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    
    # pencere oluşturmak için;
    pencere = QtWidgets.QWidget()
    
    # başlık oluşturmak için;
    pencere.setWindowTitle("PyQt5 Ders 1")
    
    # pencereye horizontal box'u ekliyebilmek için;
    # pencere.setLayout(h_box)
    pencere.setLayout(v_box)
    
    # pencerenin büyüklüğünü belirlemek için(opsiyonel);
    pencere.setGeometry(100, 100, 500, 500)
    
    # pencereyi göstermek için;
    pencere.show()
    
    # çarpıya basmadığımız sürece uygulamayı çalıştırması için;
    sys.exit(app.exec_())
    
Pencere()