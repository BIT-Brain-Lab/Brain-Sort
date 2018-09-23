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

class Ui_Dialog_lasso(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog_lasso,self).__init__()
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

        self.alpha = QtGui.QLabel(Dialog)
        self.alpha.setGeometry(QtCore.QRect(91, 111, 54, 16))
        self.alpha.setObjectName(_fromUtf8("label"))
        self.alpha.setStyleSheet('font-family:Helvetica;font-size:14px;')

        self.lineEdit_alpha = QtGui.QLineEdit(Dialog)
        self.lineEdit_alpha.setGeometry(QtCore.QRect(151, 111, 133, 20))
        self.lineEdit_alpha.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_alpha.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.loop_num = QtGui.QLabel(Dialog)
        self.loop_num.setGeometry(QtCore.QRect(91, 141, 54, 16))
        self.loop_num.setObjectName(_fromUtf8("label"))
        self.loop_num.setStyleSheet('font-family:Helvetica;font-size:14px;')

        self.lineEdit_loop_num = QtGui.QLineEdit(Dialog)
        self.lineEdit_loop_num.setGeometry(QtCore.QRect(151, 141, 133, 20))
        self.lineEdit_loop_num.setObjectName(_fromUtf8("lineEdit_p"))
        self.lineEdit_loop_num.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.retranslateUi(Dialog)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "lasso", None))
        self.alpha.setText(_translate("Dialog", "alpha", None))
        self.loop_num.setText(_translate("Dialog", "loop", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Dialog_lasso()
    win.show()
    app.exec_()
