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

class Ui_Dialog_rf(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog_rf,self).__init__()
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

        self.label_n_estimators = QtGui.QLabel(Dialog)
        self.label_n_estimators.setGeometry(QtCore.QRect(71, 91, 74, 16))
        self.label_n_estimators.setObjectName(_fromUtf8("n trees"))
        self.label_n_estimators.setStyleSheet('font-family:Helvetica;font-size:14px;')

        self.lineEdit_n_estimators = QtGui.QLineEdit(Dialog)
        self.lineEdit_n_estimators.setGeometry(QtCore.QRect(151, 91, 133, 20))
        self.lineEdit_n_estimators.setObjectName(_fromUtf8("lineEdit_n_estimators"))
        self.lineEdit_n_estimators.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.label_min_samples_split = QtGui.QLabel(Dialog)
        self.label_min_samples_split.setGeometry(QtCore.QRect(71, 121, 74, 16))
        self.label_min_samples_split.setObjectName(_fromUtf8("label_min_samples_split"))
        self.label_min_samples_split.setStyleSheet('font-family:Helvetica;font-size:14px;')

        self.lineEdit_min_samples_split = QtGui.QLineEdit(Dialog)
        self.lineEdit_min_samples_split.setGeometry(QtCore.QRect(151, 121, 133, 20))
        self.lineEdit_min_samples_split.setObjectName(_fromUtf8("lineEdit_min_samples_split"))
        self.lineEdit_min_samples_split.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')

        self.label_k_save = QtGui.QLabel(Dialog)
        self.label_k_save.setGeometry(QtCore.QRect(71, 151, 74, 16))
        self.label_k_save.setObjectName(_fromUtf8("label_k_save"))
        self.label_k_save.setStyleSheet('font-family:Helvetica;font-size:14px;')

        self.lineEdit_k_save = QtGui.QLineEdit(Dialog)
        self.lineEdit_k_save.setGeometry(QtCore.QRect(151, 151, 133, 20))
        self.lineEdit_k_save.setObjectName(_fromUtf8("lineEdit_k_save"))
        self.lineEdit_k_save.setStyleSheet(
            'border: 1px solidrgba(31, 53, 127, 0.16);border - radius: 1px;width: 239px;height: 38px;')


        self.retranslateUi(Dialog)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "random forest", None))
        self.label_n_estimators.setText(_translate("Dialog", "n trees", None))
        self.label_min_samples_split.setText(_translate("Dialog", "min split", None))
        self.label_k_save.setText(_translate("Dialog", "k features", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Dialog_rf()
    win.show()
    app.exec_()
