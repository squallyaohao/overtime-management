# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dev\overtime-management\ui_newProjectDialog.ui'
#
# Created: Sun Sep 17 00:29:37 2017
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

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(535, 512)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(535, 512))
        Dialog.setMaximumSize(QtCore.QSize(535, 512))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 41, 476, 451))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.project_name = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.project_name.setFont(font)
        self.project_name.setText(_fromUtf8(""))
        self.project_name.setObjectName(_fromUtf8("project_name"))
        self.horizontalLayout_3.addWidget(self.project_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.start_date = QtGui.QDateEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_date.setFont(font)
        self.start_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_date.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.start_date.setObjectName(_fromUtf8("start_date"))
        self.start_date.setDisplayFormat('yyyy-MM-dd')
        self.start_date.setCalendarPopup(True)
        self.horizontalLayout.addWidget(self.start_date)
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setText(_fromUtf8(""))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout.addWidget(self.label_17)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.finish_date = QtGui.QDateEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.finish_date.setFont(font)
        self.finish_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.finish_date.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.finish_date.setObjectName(_fromUtf8("finish_date"))
        self.finish_date.setDisplayFormat('yyyy-MM-dd')
        self.finish_date.setCalendarPopup(True)
        self.horizontalLayout.addWidget(self.finish_date)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout.addWidget(self.label_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_3.addWidget(self.label_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.product_PM = QtGui.QLineEdit(self.layoutWidget)
        self.product_PM.setObjectName(_fromUtf8("product_PM"))
        self.horizontalLayout_4.addWidget(self.product_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.script_PM = QtGui.QLineEdit(self.layoutWidget)
        self.script_PM.setObjectName(_fromUtf8("script_PM"))
        self.horizontalLayout_5.addWidget(self.script_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.design_PM = QtGui.QLineEdit(self.layoutWidget)
        self.design_PM.setObjectName(_fromUtf8("design_PM"))
        self.horizontalLayout_6.addWidget(self.design_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.flash_PM = QtGui.QLineEdit(self.layoutWidget)
        self.flash_PM.setObjectName(_fromUtf8("flash_PM"))
        self.horizontalLayout_7.addWidget(self.flash_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.ani_PM = QtGui.QLineEdit(self.layoutWidget)
        self.ani_PM.setObjectName(_fromUtf8("ani_PM"))
        self.horizontalLayout_8.addWidget(self.ani_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.post_PM = QtGui.QLineEdit(self.layoutWidget)
        self.post_PM.setObjectName(_fromUtf8("post_PM"))
        self.horizontalLayout_9.addWidget(self.post_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_11.addWidget(self.label_10)
        self.software_PM = QtGui.QLineEdit(self.layoutWidget)
        self.software_PM.setObjectName(_fromUtf8("software_PM"))
        self.horizontalLayout_11.addWidget(self.software_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.hardware_PM = QtGui.QLineEdit(self.layoutWidget)
        self.hardware_PM.setObjectName(_fromUtf8("hardware_PM"))
        self.horizontalLayout_12.addWidget(self.hardware_PM)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_13.addWidget(self.label_16)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.project_desc = QtGui.QPlainTextEdit(self.layoutWidget)
        self.project_desc.setObjectName(_fromUtf8("project_desc"))
        self.verticalLayout_2.addWidget(self.project_desc)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "新建项目", None))
        self.label.setText(_translate("Dialog", "项目名称", None))
        self.label_2.setText(_translate("Dialog", "起始时间", None))
        self.label_3.setText(_translate("Dialog", "结束时间", None))
        self.label_7.setText(_translate("Dialog", "项目经理", None))
        self.label_4.setText(_translate("Dialog", "脚本负责", None))
        self.label_5.setText(_translate("Dialog", "平面负责", None))
        self.label_6.setText(_translate("Dialog", "二维负责", None))
        self.label_8.setText(_translate("Dialog", "三维负责", None))
        self.label_9.setText(_translate("Dialog", "后期负责", None))
        self.label_10.setText(_translate("Dialog", "软件负责", None))
        self.label_11.setText(_translate("Dialog", "硬件负责", None))
        self.label_12.setText(_translate("Dialog", "项目说明", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.show()
    app.exec_()
