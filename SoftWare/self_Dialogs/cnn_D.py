# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\cnn.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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


class Ui_Dialog_CNN(QtGui.QDialog):

    def __init__(self):
        super(Ui_Dialog_CNN, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(476, 362)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 56, 42, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 97, 42, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 138, 42, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 178, 42, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 219, 54, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 54, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.cov1 = QtGui.QLineEdit(Dialog)
        self.cov1.setGeometry(QtCore.QRect(90, 55, 133, 20))
        self.cov1.setObjectName(_fromUtf8("cov1"))
        self.cov1.setText('5 5 64 1 1')
        self.pool1 = QtGui.QLineEdit(Dialog)
        self.pool1.setGeometry(QtCore.QRect(90, 96, 133, 20))
        self.pool1.setText(_fromUtf8(""))
        self.pool1.setObjectName(_fromUtf8("pool1"))
        self.pool1.setText('3 3 2 2')
        self.cov2 = QtGui.QLineEdit(Dialog)
        self.cov2.setGeometry(QtCore.QRect(90, 137, 133, 20))
        self.cov2.setText(_fromUtf8(""))
        self.cov2.setObjectName(_fromUtf8("cov2"))
        self.cov2.setText('5 5 64 1 1')
        self.pool2 = QtGui.QLineEdit(Dialog)
        self.pool2.setGeometry(QtCore.QRect(90, 178, 133, 20))
        self.pool2.setText(_fromUtf8(""))
        self.pool2.setObjectName(_fromUtf8("pool2"))
        self.pool2.setText('3 3 2 2')
        self.fc1 = QtGui.QLineEdit(Dialog)
        self.fc1.setGeometry(QtCore.QRect(90, 219, 133, 20))
        self.fc1.setText(_fromUtf8(""))
        self.fc1.setObjectName(_fromUtf8("fc1"))
        self.fc1.setText('128')
        self.fc2 = QtGui.QLineEdit(Dialog)
        self.fc2.setGeometry(QtCore.QRect(90, 260, 133, 20))
        self.fc2.setText(_fromUtf8(""))
        self.fc2.setObjectName(_fromUtf8("fc2"))
        self.fc2.setText('32')
        self.kfold = QtGui.QLineEdit(Dialog)
        self.kfold.setGeometry(QtCore.QRect(331, 57, 133, 20))
        self.kfold.setObjectName(_fromUtf8("kfold"))
        self.kfold.setText('3')
        self.learning_rate = QtGui.QLineEdit(Dialog)
        self.learning_rate.setGeometry(QtCore.QRect(331, 99, 133, 20))
        self.learning_rate.setText(_fromUtf8(""))
        self.learning_rate.setObjectName(_fromUtf8("learning_rate"))
        self.learning_rate.setText('0.01')
        self.batch = QtGui.QLineEdit(Dialog)
        self.batch.setGeometry(QtCore.QRect(331, 141, 133, 20))
        self.batch.setText(_fromUtf8(""))
        self.batch.setObjectName(_fromUtf8("batch"))
        self.batch.setText('50')
        self.epoch = QtGui.QLineEdit(Dialog)
        self.epoch.setGeometry(QtCore.QRect(331, 183, 133, 20))
        self.epoch.setText(_fromUtf8(""))
        self.epoch.setObjectName(_fromUtf8("epoch"))
        self.epoch.setText('1')
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(260, 56, 36, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(260, 97, 48, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(260, 140, 30, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(260, 190, 30, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Conv1", None))
        self.label_2.setText(_translate("Dialog", "Pool1", None))
        self.label_3.setText(_translate("Dialog", "Conv2", None))
        self.label_5.setText(_translate("Dialog", "Pool2", None))
        self.label_6.setText(_translate("Dialog", "FC1", None))
        self.label_7.setText(_translate("Dialog", "FC2", None))
        self.label_10.setText(_translate("Dialog", "K-Fold", None))
        self.label_9.setText(_translate("Dialog", "L-Rate", None))
        self.label_8.setText(_translate("Dialog", "Batch", None))
        self.label_11.setText(_translate("Dialog", "Epoch", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Dialog_CNN()
    win.show()
    app.exec_()