# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python27\ui_mainwindow.ui'
#
# Created: Sun Sep 10 23:10:28 2017
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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(620, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(620, 400))
        MainWindow.setMaximumSize(QtCore.QSize(620, 400))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 581, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 170, 100, 40))
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 536, 32))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(40, 30))
        self.label.setMaximumSize(QtCore.QSize(40, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.apply_date = QtGui.QDateEdit(self.layoutWidget)
        self.apply_date.setMaximumSize(QtCore.QSize(16777215, 30))
        self.apply_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.apply_date.setObjectName(_fromUtf8("apply_date"))
        self.horizontalLayout_2.addWidget(self.apply_date)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(70, 30))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.apply_duration = QtGui.QSpinBox(self.layoutWidget)
        self.apply_duration.setMinimumSize(QtCore.QSize(0, 30))
        self.apply_duration.setMaximumSize(QtCore.QSize(16777215, 30))
        self.apply_duration.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.apply_duration.setObjectName(_fromUtf8("apply_duration"))
        self.horizontalLayout_2.addWidget(self.apply_duration)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 30))
        self.label_4.setMaximumSize(QtCore.QSize(50, 30))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.apply_meal = QtGui.QLineEdit(self.layoutWidget)
        self.apply_meal.setMinimumSize(QtCore.QSize(0, 30))
        self.apply_meal.setMaximumSize(QtCore.QSize(16777215, 30))
        self.apply_meal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.apply_meal.setObjectName(_fromUtf8("apply_meal"))
        self.horizontalLayout_2.addWidget(self.apply_meal)
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 100, 531, 32))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setMinimumSize(QtCore.QSize(60, 30))
        self.label_2.setMaximumSize(QtCore.QSize(40, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.apply_project = QtGui.QComboBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_project.sizePolicy().hasHeightForWidth())
        self.apply_project.setSizePolicy(sizePolicy)
        self.apply_project.setMinimumSize(QtCore.QSize(0, 30))
        self.apply_project.setMaximumSize(QtCore.QSize(16777215, 30))
        self.apply_project.setEditable(False)
        self.apply_project.setObjectName(_fromUtf8("apply_project"))
        self.horizontalLayout_3.addWidget(self.apply_project)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 170, 100, 40))
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.layoutWidget2 = QtGui.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 363, 32))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(40, 30))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.query_fromdate = QtGui.QDateEdit(self.layoutWidget2)
        self.query_fromdate.setMinimumSize(QtCore.QSize(0, 30))
        self.query_fromdate.setMaximumSize(QtCore.QSize(16777215, 30))
        self.query_fromdate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.query_fromdate.setObjectName(_fromUtf8("query_fromdate"))
        self.horizontalLayout_4.addWidget(self.query_fromdate)
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(30, 30))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setMidLineWidth(0)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.query_todate = QtGui.QDateEdit(self.layoutWidget2)
        self.query_todate.setMinimumSize(QtCore.QSize(0, 30))
        self.query_todate.setMaximumSize(QtCore.QSize(16777215, 30))
        self.query_todate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.query_todate.setObjectName(_fromUtf8("query_todate"))
        self.horizontalLayout_4.addWidget(self.query_todate)
        self.layoutWidget3 = QtGui.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 100, 441, 32))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(40, 0))
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.query_project = QtGui.QComboBox(self.layoutWidget3)
        self.query_project.setMinimumSize(QtCore.QSize(0, 30))
        self.query_project.setMaximumSize(QtCore.QSize(16777215, 30))
        self.query_project.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.query_project.setObjectName(_fromUtf8("query_project"))
        self.query_project.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.query_project)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.layoutWidget4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 10, 580, 61))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.name = QtGui.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        self.name.setFont(font)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.name_line = QtGui.QLineEdit(self.layoutWidget4)
        self.name_line.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        self.name_line.setFont(font)
        self.name_line.setObjectName(_fromUtf8("name_line"))
        self.horizontalLayout.addWidget(self.name_line)
        self.pushButton = QtGui.QPushButton(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.name_2 = QtGui.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        self.name_2.setFont(font)
        self.name_2.setObjectName(_fromUtf8("name_2"))
        self.horizontalLayout.addWidget(self.name_2)
        self.comboBox = QtGui.QComboBox(self.layoutWidget4)
        self.comboBox.setEnabled(False)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Apply Overtime", None))
        self.pushButton_3.setText(_translate("MainWindow", "Confirm", None))
        self.label.setText(_translate("MainWindow", "Date", None))
        self.label_3.setText(_translate("MainWindow", "Duration", None))
        self.label_4.setText(_translate("MainWindow", "Meal", None))
        self.label_2.setText(_translate("MainWindow", "Project", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Apply", None))
        self.pushButton_4.setText(_translate("MainWindow", "Start Query", None))
        self.label_5.setText(_translate("MainWindow", "From", None))
        self.query_fromdate.setDisplayFormat(_translate("MainWindow", "yyyy-M-d", None))
        self.label_6.setText(_translate("MainWindow", "To", None))
        self.query_todate.setDisplayFormat(_translate("MainWindow", "yyyy-M-d", None))
        self.label_7.setText(_translate("MainWindow", "Project", None))
        self.query_project.setItemText(0, _translate("MainWindow", "*", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Query", None))
        self.name.setText(_translate("MainWindow", "name", None))
        self.pushButton.setText(_translate("MainWindow", "edit", None))
        self.name_2.setText(_translate("MainWindow", "Department", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "三维动画", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "投标动画", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "二维动画", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "平面设计", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "编导", None))
        self.pushButton_2.setText(_translate("MainWindow", "edit", None))




