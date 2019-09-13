# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:41:47 2019

@author: Sefa3
"""

import sys
import os

from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow

class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        # bir menübar yarattık.
        menubar = self.menuBar()
        
        # menübara 'dosya' ve 'duzenle' isimli iki menü ekledik.
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")
        
        # 'dosya_ac' isimli bir action yarattık.
        dosya_ac = QAction("Dosya Aç", self)
        dosya_ac.setShortcut("Ctrl+O")
        
        # 'dosya_kaydet' isimli bir action yarattık.
        dosya_kaydet = QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        
        # 'cikis' isimli bir action yarattık.
        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")
        
        # dosya menüsüne 'dosya_ac', 'dosya_kaydet', 'cikis' actionlarını ekledik.
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)
        
        # 'duzenle' menüsünün içerisine 'ara_ve_degistir' isimli alt menü eklemek için;
        ara_ve_degistir = duzenle.addMenu("Ara ve Değiştir")
        
        # 'Ara' isimli action yarattık.
        ara = QAction("Ara", self)
        
        # 'Degiştir' isimli action yarattık.
        degistir = QAction("Değiştir", self)
        
        temizle = QAction("Temizle", self)
        
        # 'Ara ve Değiştir' adlı alt menübara 'Ara' ve 'Değiştir' actionlarını ekledik.
        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)
        
        duzenle.addAction(temizle)
        
        cikis.triggered.connect(self.cikis_yap)
        
        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menüler")
        
        self.show()
        
    
    def cikis_yap(self):
        qApp.quit()
    
    # python aslında yukarıda yazdığımız yere bir action objesi gönderdi.
    # bu yüzden bizde bu action objesini fonksiyona ekliyoruz.
    def response(self, action):
        if action.text() == "Dosya Aç":
            print("Dosya Aç'a basıldı.")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e basıldı.")
        elif action.text() == "Çıkış":
            print("Çıkış'a basıldı.")
        
app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())