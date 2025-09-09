import sys
import pygame
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton) # for vertical horizontal and grid layout
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import QTimer, QTime, Qt
from pygame.examples.go_over_there import clock


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initui()
    def initui(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px;"
                                      
                                      "color: green;")
        self.setStyleSheet("background-color:black;") # for background color of the gui
        font_id=QFontDatabase.addApplicationFont("DS-DIGIT.TTF")#Managing custom fonts available to the application and adding them. Here we are adding a custom font
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0] # returns the first font
        my_font=QFont(font_family,150) #acessing font
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time) #it will join with the update_time and trigger a timeout after 1000 milisecond
        self.timer.start(1000) # it will update the timer after 1000 milisecond
        self.update_time() #calling function to display the current time
    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP") #
        self.time_label.setText(current_time) #set text of the label


if __name__=="__main__":
    app = QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())

