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

class Ui_Dialog_elastic_network(QtGui.QDialog):

    def __init__(self):
        super(Ui_Dialog_elastic_network,self).__init__()
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
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

        self.label_alpha = QtGui.QLabel(Dialog)
        self.label_alpha.setGeometry(QtCore.QRect(71, 91, 70, 16))
        self.label_alpha.setObjectName(_fromUtf8("alpha"))
        self.label_alpha.setStyleSheet('font-family:Helvetica;font-size:14px;')
        self.lineEdit_alpha = QtGui.QLineEdit(Dialog)
        self.lineEdit_alpha.setGeometry(QtCore.QRect(150, 91, 133, 20))
        self.lineEdit_alpha.setObjectName(_fromUtf8("lineEdit_alpha"))
        self.lineEdit_alpha.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.label_l1_ratio = QtGui.QLabel(Dialog)
        self.label_l1_ratio.setGeometry(QtCore.QRect(71, 121, 70, 16))
        self.label_l1_ratio.setObjectName(_fromUtf8("label_l1_ratio"))
        self.label_l1_ratio.setStyleSheet('font-family:Helvetica;font-size:14px;')
        self.lineEdit_l1_ratio = QtGui.QLineEdit(Dialog)
        self.lineEdit_l1_ratio.setGeometry(QtCore.QRect(150, 121, 133, 20))
        self.lineEdit_l1_ratio.setObjectName(_fromUtf8("lineEdit_l1_ratio"))
        self.lineEdit_l1_ratio.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.label_max_iter = QtGui.QLabel(Dialog)
        self.label_max_iter.setGeometry(QtCore.QRect(71, 151, 70, 16))
        self.label_max_iter.setObjectName(_fromUtf8("label_max_iter"))
        self.label_max_iter.setStyleSheet('font-family:Helvetica;font-size:14px;')
        self.lineEdit_max_iter = QtGui.QLineEdit(Dialog)
        self.lineEdit_max_iter.setGeometry(QtCore.QRect(150, 151, 133, 20))
        self.lineEdit_max_iter.setObjectName(_fromUtf8("lineEdit_max_iter"))
        self.lineEdit_max_iter.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.label_tol = QtGui.QLabel(Dialog)
        self.label_tol.setGeometry(QtCore.QRect(71, 181, 70, 16))
        self.label_tol.setObjectName(_fromUtf8("label_tol"))
        self.label_tol.setStyleSheet('font-family:Helvetica;font-size:14px;')
        self.lineEdit_tol = QtGui.QLineEdit(Dialog)
        self.lineEdit_tol.setGeometry(QtCore.QRect(150, 181, 133, 20))
        self.lineEdit_tol.setObjectName(_fromUtf8("lineEdit_tol"))
        self.lineEdit_tol.setStyleSheet('border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.retranslateUi(Dialog)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Elasticity Net", None))
        self.label_alpha.setText(_translate("Dialog", "alpha", None))
        self.label_l1_ratio.setText(_translate("Dialog", "l1 ratio", None))
        self.label_max_iter.setText(_translate("Dialog", "max loop", None))
        self.label_tol.setText(_translate("Dialog", "tolerance", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Dialog_elastic_network()
    win.show()
    app.exec_()
