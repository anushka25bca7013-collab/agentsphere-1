#push button in gui

import sys


from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,QPushButton,QLineEdit) # for vertical horizontal and grid layout
from PyQt5.QtGui import QIcon #for icon of gui

class MainWindow(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")# gui name
        self.setGeometry(700,300,500,500) # gui window
        self.setWindowIcon(QIcon("App.png"))# gui pic
        self.edit_Line=QLineEdit(self)
        self.button=QPushButton("Submit",self)


        self.initui()

    def initui(self):
        self.edit_Line.setGeometry(10,10,200,40)
        self.edit_Line.setStyleSheet("font-family:Times New Roman;"
                                    "font-size: 25px;")
        self.button.setGeometry(210,10,200,40)
        self.button.setStyleSheet("font-family: Arial;"
                                  "font-size: 30px;")
        self.edit_Line.setPlaceholderText("Enter your name") #for place holder text
        self.button.clicked.connect(self.submit)
    def submit(self):
        text=self.edit_Line.text()# to access the text written in the textbox of edit_line
        print(f"Hello {text}")



def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()



