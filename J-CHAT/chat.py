from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QSize
from details import Ui_Dialog
import qtmodern.styles
import qtmodern.windows
import pickle
import os
import sys
import random


class Ui_MainWindow(QMainWindow):
    
    def closeEvent(self, event):
         print("Closing chat")
         self.remove_online()
         sys.exit()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 628)
        self.user="Unknown"
        self.initator=0
        self.chtmd=os.path.getmtime("dbs")-1
        self.onmd=os.path.getmtime("online")-1
     
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 721, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.nicks = QtWidgets.QListWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nicks.sizePolicy().hasHeightForWidth())
        self.nicks.setSizePolicy(sizePolicy)
        self.nicks.setObjectName("nicks online")
        self.gridLayout.addWidget(self.nicks, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.setStyleSheet("QPushButton {background-color: none; border: 1px solid black}")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("QTextEdit{background-image: url(bg2.png);}")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(True)
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.ensureCursorVisible()
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.shortcut_enter = QShortcut(Qt.Key_Return, self)
        self.shortcut_enter.activated.connect(self.sender)
        

        self.cmds=["clear;"]
        self.colors=["red","white","yellow","orange","violet","aqua","cyan","lime"]
        self.mycolor="<font color=\""+random.choice(self.colors)+"\">"
        self.generalStyle='''<font size=5><font style="font-family: Trebuchet MS">'''
        
       

        
        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.update_chat)
        self._update_timer.start(100)
       


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "J CHAT"))
        self.pushButton.setText(_translate("MainWindow", "send"))
        self.pushButton.clicked.connect(self.sender)
        self.pushButton_2.clicked.connect(self.openCredit)
        
        self.pushButton_2.setText(_translate("MainWindow", "credits"))

    def openCredit(self):
            self.credits = QtWidgets.QApplication([])
            self.Details = QtWidgets.QDialog()
            self.uidet = Ui_Dialog()
            self.uidet.setupUi(self.Details)
            
            self.Details.show()

            qtmodern.styles.dark(self.credits)
            self.mw2 = qtmodern.windows.ModernWindow(self.Details)
            self.mw2.show()
            self.shortcut_enter = QShortcut(Qt.Key_Return, self)
            self.shortcut_enter.activated.connect(self.sender)
            
            
            

    def addonline(self):
        with open("online","a") as f:
            f.write(self.user+"\n")    
        
        
        
    def remove_online(self):
        with open("online", "r") as f:
            lines = f.readlines()
        with open("online", "w") as f:
            for line in lines:
                if (line.strip("\n") != self.user):
                    f.write(line)
              

    def moddata(self,data):
        if("(#cmd)") in data:
            data=data.replace("(#cmd)","")
            return data
        data=data.replace("&","&amp;")
        data=data.replace("<","&lt;")
        data=data.replace(">","&gt;")
        


        return data
    
    def sender(self):
        data=self.lineEdit.text()
        if(data in self.cmds):
            self.SU(data)
        else:
            data=self.moddata(data)
            with open("dbs","a") as f:
                if(self.initator==0):
                    self.initator=1
                    f.write(self.generalStyle)
                f.write("<br>"+self.mycolor+"<i><b>"+self.user.upper()+"</b> : "+data+"</i>")
        self.lineEdit.clear()


    
    def update_chat(self):
        xchtmd=os.path.getmtime("dbs")
        self.update_online()
        if(xchtmd ==self.chtmd):
            return
        self.chtmd=xchtmd
        
        with open("dbs","r") as f:
            data=f.read()
            self
            self.textBrowser.setHtml(data)
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
            self.textBrowser.ensureCursorVisible()
        
    def update_online(self):
        xchtmdx=os.path.getmtime("online")
        if(xchtmdx ==self.onmd):
            return
        self.onmd=xchtmdx
        
        
        
        lis=[]
        with open("online","r") as f:
            lis=f.read().split("\n")
        lis=[x.upper() for x in lis]
        self.nicks.clear()
        self.nicks.addItems(lis)
        self.nicks.show()
        


    def  SU(self,cmd):
        if(cmd=="clear;"):
            with open("dbs","r+") as f:
                f.truncate(0)
    

    
        





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    
    
    sys.exit(app.exec_())
