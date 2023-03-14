import sys
from tkinter import Widget
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
    )
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from loginui import Ui_Dialog
import json
from historyui import demo2
# import weather
from weatherui import Demo, Ui_weatherui, canvas

with open('user.json','r') as fin:
    data = json.load(fin)
class Login(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.checkBox.stateChanged.connect(self.b_RememberInfo)
        self.pushButton.clicked.connect(self.Login)
        # self.pushButton1.clicked.connect(self.gotohistory)

    def Login(self):
        ##
        flag = 0
        n = self.GetUserName()
        p = self.Getpassword()
        for i in range(len(data['username'])):
            if n==data['username'][i]:
                if p==data["password"][i]:
                    flag = 1
                    QMessageBox.about(self,"notification","login successfully!!")
                    break             
            else:
                data['username'].append(n)
                data['password'].append(p)
                with open('user.json','w') as fin:
                    fin.write(json.dumps(data))
                break
        if(flag == 1):
            self.gotoweather()
 
    def b_RememberInfo(self):
        return self.checkBox.isChecked()

    def GetUserName(self):
        username = self.textEdit.toPlainText()
        return username
    def Getpassword(self):
        password = self.textEdit_2.toPlainText()
        return password
    def gotoweather(self):
        weather = Demo()
        widget.addWidget(weather)
        widget.setCurrentIndex(widget.currentIndex()+1)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(login)
    widget.setFixedHeight(700)
    widget.setFixedWidth(1600)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")