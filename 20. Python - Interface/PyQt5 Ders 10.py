# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:09:35 2019

@author: Sefa3
"""

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        
        v_box = QVBoxLayout()
        
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        
        self.setWindowTitle("Yazı Alanı")
        
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.show()
        
    def click(self):
        self.yazi_alani.clear()
        
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())