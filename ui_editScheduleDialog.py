# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\dev\overtime-management\ui_editScheduleDialog.ui'
#
# Created: Fri Feb 15 15:47:20 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(550, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(550, 150))
        Dialog.setMaximumSize(QtCore.QSize(550, 150))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 511, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.itemName = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemName.sizePolicy().hasHeightForWidth())
        self.itemName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        self.itemName.setFont(font)
        self.itemName.setObjectName(_fromUtf8("itemName"))
        self.verticalLayout.addWidget(self.itemName)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startDateLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDateLabel.sizePolicy().hasHeightForWidth())
        self.startDateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(12)
        self.startDateLabel.setFont(font)
        self.startDateLabel.setObjectName(_fromUtf8("startDateLabel"))
        self.horizontalLayout.addWidget(self.startDateLabel)
        self.startDate = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.horizontalLayout.addWidget(self.startDate)
        self.endDateLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endDateLabel.sizePolicy().hasHeightForWidth())
        self.endDateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(12)
        self.endDateLabel.setFont(font)
        self.endDateLabel.setObjectName(_fromUtf8("endDateLabel"))
        self.horizontalLayout.addWidget(self.endDateLabel)
        self.endDate = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.horizontalLayout.addWidget(self.endDate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "编辑内容", None))
        self.itemName.setText(_translate("Dialog", "TextLabel", None))
        self.startDateLabel.setText(_translate("Dialog", "起始时间", None))
        self.startDate.setDisplayFormat(_translate("Dialog", "yyyy-M-d", None))
        self.endDateLabel.setText(_translate("Dialog", "结束时间", None))
        self.endDate.setDisplayFormat(_translate("Dialog", "yyyy-M-d", None))

