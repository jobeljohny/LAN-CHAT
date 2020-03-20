# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailsui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 226)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 421, 171))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 151))
        self.label.setObjectName("label")
        self.pixmap = QPixmap('prf.rar')
        self.label.setPixmap(self.pixmap.scaled(
            self.label.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "JOBEL JOHNY"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Hey there and Welcome!</span></p><p align=\"justify\"><span style=\" font-weight:600;\">I\'m Jobel Johny, Developer of J-Chat. Help us build a stronger community. </span></p><p align=\"justify\"><span style=\" font-weight:600;\">Suggestions and Corrections are Always Welcome!</span></p><p align=\"justify\"><span style=\" font-weight:600;\">Instagram :</span><a href=\"https://www.instagram.com/dank_maven/\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\"> Go to Profile</span></a></p><p align=\"justify\"><span style=\" font-weight:600;\">your feedback is as important as you, contact me through,</span></p><p align=\"justify\"><span style=\" font-weight:600;\">E-mail : jobeljohny@gmail.com</span></p><p align=\"justify\"><span style=\" font-weight:600;\">Thank you ! and have a nice day!</span></p></body></html>"))
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
