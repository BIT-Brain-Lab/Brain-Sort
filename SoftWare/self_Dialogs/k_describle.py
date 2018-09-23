# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linear_D.ui'
#
# Created: Wed Mar 01 16:20:50 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))

class Ui_Dialog_k_desc(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog_k_desc,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.buttonBox.setStyleSheet('font-family:Helvetica;font-size:15px;background-image:linear-gradient(-90deg, #05e0fa 0%, rgba(1,189,242,0.00) 100%);')

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(91, 121, 54, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet('font-family:Helvetica;font-size:14px;')

        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(151, 121, 133, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')
        self.retranslateUi(Dialog)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "plot K", None))
        self.label.setText(_translate("Dialog", "K", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Dialog_k_desc()
    win.show()
    app.exec_()