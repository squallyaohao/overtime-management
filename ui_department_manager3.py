# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dev\overtime-management\ui_department_manager3.ui'
#
# Created: Tue Sep 19 22:59:18 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import newTable

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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1138, 804)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(620, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1138, 804))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(_fromUtf8(""))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 25, 1116, 746))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.layoutWidget = QtGui.QWidget(self.tab1)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 50, 1086, 666))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_32 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.verticalLayout.addWidget(self.label_32)
        self.tree_project = QtGui.QTreeWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_project.sizePolicy().hasHeightForWidth())
        self.tree_project.setSizePolicy(sizePolicy)
        self.tree_project.setMaximumSize(QtCore.QSize(250, 16777215))
        self.tree_project.setObjectName(_fromUtf8("tree_project"))
        self.tree_project.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.tree_project)
        self.delete_2 = QtGui.QPushButton(self.layoutWidget)
        self.delete_2.setObjectName(_fromUtf8("delete_2"))
        self.verticalLayout.addWidget(self.delete_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget_2 = QtGui.QTabWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_2 = QtGui.QWidget()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 15, 806, 32))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_tables = QtGui.QLabel(self.layoutWidget1)
        self.label_tables.setObjectName(_fromUtf8("label_tables"))
        self.horizontalLayout.addWidget(self.label_tables)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btn_add_project = QtGui.QPushButton(self.layoutWidget1)
        self.btn_add_project.setObjectName(_fromUtf8("btn_add_project"))
        self.horizontalLayout_6.addWidget(self.btn_add_project)
        self.btn_add_subproject = QtGui.QPushButton(self.layoutWidget1)
        self.btn_add_subproject.setObjectName(_fromUtf8("btn_add_subproject"))
        self.horizontalLayout_6.addWidget(self.btn_add_subproject)
        self.btn_add_task = QtGui.QPushButton(self.layoutWidget1)
        self.btn_add_task.setObjectName(_fromUtf8("btn_add_task"))
        self.horizontalLayout_6.addWidget(self.btn_add_task)
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        self.widget = QtGui.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(5, 60, 806, 576))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.table_prodetail = newTable.NewTable(self.widget)
        self.table_prodetail.setObjectName(_fromUtf8("table_prodetail"))
        self.table_prodetail.setColumnCount(0)
        self.table_prodetail.setRowCount(0)
        self.table_prodetail.horizontalHeader().setStretchLastSection(True)
        self.table_prodetail.verticalHeader().setVisible(True)
        self.horizontalLayout_9.addWidget(self.table_prodetail)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(500, 0))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_19.addWidget(self.label_4)
        self.btn_exportExcel = QtGui.QPushButton(self.widget)
        self.btn_exportExcel.setObjectName(_fromUtf8("btn_exportExcel"))
        self.horizontalLayout_19.addWidget(self.btn_exportExcel)
        self.btn_save = QtGui.QPushButton(self.widget)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.horizontalLayout_19.addWidget(self.btn_save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.table_schedul = newTable.NewTable(self.tab_3)
        self.table_schedul.setGeometry(QtCore.QRect(5, 60, 806, 571))
        self.table_schedul.setObjectName(_fromUtf8("table_schedul"))
        self.table_schedul.setColumnCount(0)
        self.table_schedul.setRowCount(0)
        self.layoutWidget2 = QtGui.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(650, 20, 160, 28))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.schedual_method_combo = QtGui.QComboBox(self.layoutWidget2)
        self.schedual_method_combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.schedual_method_combo.setObjectName(_fromUtf8("schedual_method_combo"))
        self.schedual_method_combo.addItem(_fromUtf8(""))
        self.schedual_method_combo.addItem(_fromUtf8(""))
        self.schedual_method_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.schedual_method_combo)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget3 = QtGui.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(14, 15, 1081, 651))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.frame_3 = QtGui.QFrame(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(160, 16777215))
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.layoutWidget4 = QtGui.QWidget(self.frame_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(5, 6, 153, 636))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_9 = QtGui.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_17 = QtGui.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_7.addWidget(self.label_17)
        self.member_name_line = QtGui.QLineEdit(self.layoutWidget4)
        self.member_name_line.setMinimumSize(QtCore.QSize(100, 25))
        self.member_name_line.setObjectName(_fromUtf8("member_name_line"))
        self.horizontalLayout_7.addWidget(self.member_name_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_18 = QtGui.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_17.addWidget(self.label_18)
        self.member_title_line = QtGui.QLineEdit(self.layoutWidget4)
        self.member_title_line.setMinimumSize(QtCore.QSize(100, 25))
        self.member_title_line.setObjectName(_fromUtf8("member_title_line"))
        self.horizontalLayout_17.addWidget(self.member_title_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.add_member_btn = QtGui.QPushButton(self.layoutWidget4)
        self.add_member_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.add_member_btn.setMaximumSize(QtCore.QSize(1000, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_member_btn.setFont(font)
        self.add_member_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_member_btn.setObjectName(_fromUtf8("add_member_btn"))
        self.horizontalLayout_18.addWidget(self.add_member_btn)
        self.delete_member_btn = QtGui.QPushButton(self.layoutWidget4)
        self.delete_member_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.delete_member_btn.setMaximumSize(QtCore.QSize(1000, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_member_btn.setFont(font)
        self.delete_member_btn.setIconSize(QtCore.QSize(30, 30))
        self.delete_member_btn.setObjectName(_fromUtf8("delete_member_btn"))
        self.horizontalLayout_18.addWidget(self.delete_member_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.member_list = QtGui.QListWidget(self.layoutWidget4)
        self.member_list.setObjectName(_fromUtf8("member_list"))
        self.verticalLayout_3.addWidget(self.member_list)
        self.horizontalLayout_12.addWidget(self.frame_3)
        self.frame = QtGui.QFrame(self.layoutWidget3)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget5 = QtGui.QWidget(self.frame)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 5, 909, 641))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtGui.QLabel(self.layoutWidget5)
        self.label_11.setMinimumSize(QtCore.QSize(350, 0))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(self.layoutWidget5)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(3)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.assigned_task = QtGui.QTreeWidget(self.layoutWidget5)
        self.assigned_task.setObjectName(_fromUtf8("assigned_task"))
        self.assigned_task.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_5.addWidget(self.assigned_task)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_12 = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setIndent(3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_7.addWidget(self.label_12)
        self.table_memberDaily = QtGui.QTableWidget(self.layoutWidget5)
        self.table_memberDaily.setColumnCount(4)
        self.table_memberDaily.setHorizontalHeaderLabels([u'日期',u'时长',u'事项',u'备注'])
        self.table_memberDaily.setObjectName(_fromUtf8("table_memberDaily"))
        self.verticalLayout_7.addWidget(self.table_memberDaily)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.layoutWidget6 = QtGui.QWidget(self.tab2)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 40, 1085, 656))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.query_member = QtGui.QComboBox(self.layoutWidget6)
        self.query_member.setMinimumSize(QtCore.QSize(0, 20))
        self.query_member.setMaximumSize(QtCore.QSize(16777215, 25))
        self.query_member.setObjectName(_fromUtf8("query_member"))
        self.query_member.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.query_member)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(20, 20))
        self.label_5.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.query_fromdate = QtGui.QDateEdit(self.layoutWidget6)
        self.query_fromdate.setMinimumSize(QtCore.QSize(100, 20))
        self.query_fromdate.setMaximumSize(QtCore.QSize(100, 20))
        self.query_fromdate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.query_fromdate.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.query_fromdate.setObjectName(_fromUtf8("query_fromdate"))
        self.horizontalLayout_4.addWidget(self.query_fromdate)
        self.label_6 = QtGui.QLabel(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(20, 20))
        self.label_6.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setMidLineWidth(0)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.query_todate = QtGui.QDateEdit(self.layoutWidget6)
        self.query_todate.setMinimumSize(QtCore.QSize(0, 20))
        self.query_todate.setMaximumSize(QtCore.QSize(100, 20))
        self.query_todate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.query_todate.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.query_todate.setObjectName(_fromUtf8("query_todate"))
        self.horizontalLayout_4.addWidget(self.query_todate)
        self.label_14 = QtGui.QLabel(self.layoutWidget6)
        self.label_14.setMinimumSize(QtCore.QSize(400, 0))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_4.addWidget(self.label_14)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.query_project = QtGui.QComboBox(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_project.sizePolicy().hasHeightForWidth())
        self.query_project.setSizePolicy(sizePolicy)
        self.query_project.setMinimumSize(QtCore.QSize(0, 20))
        self.query_project.setMaximumSize(QtCore.QSize(16777215, 25))
        self.query_project.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.query_project.setObjectName(_fromUtf8("query_project"))
        self.query_project.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.query_project)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_5)
        self.label_15 = QtGui.QLabel(self.layoutWidget6)
        self.label_15.setMinimumSize(QtCore.QSize(30, 0))
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_15.addWidget(self.label_15)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_13 = QtGui.QLabel(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.label_13.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_13.addWidget(self.label_13)
        self.query_subproject = QtGui.QComboBox(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_subproject.sizePolicy().hasHeightForWidth())
        self.query_subproject.setSizePolicy(sizePolicy)
        self.query_subproject.setMinimumSize(QtCore.QSize(0, 20))
        self.query_subproject.setMaximumSize(QtCore.QSize(16777215, 25))
        self.query_subproject.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.query_subproject.setObjectName(_fromUtf8("query_subproject"))
        self.query_subproject.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.query_subproject)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        self.query = QtGui.QPushButton(self.layoutWidget6)
        self.query.setMinimumSize(QtCore.QSize(100, 25))
        self.query.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.query.setFont(font)
        self.query.setObjectName(_fromUtf8("query"))
        self.horizontalLayout_15.addWidget(self.query)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.query_overtime_table = newTable.NewTable(self.layoutWidget6)
        self.query_overtime_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.query_overtime_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.query_overtime_table.setObjectName(_fromUtf8("query_overtime_table"))
        self.query_overtime_table.setColumnCount(0)
        self.query_overtime_table.setRowCount(0)
        self.query_overtime_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_10.addWidget(self.query_overtime_table)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_16 = QtGui.QLabel(self.layoutWidget6)
        self.label_16.setMinimumSize(QtCore.QSize(900, 0))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_16.addWidget(self.label_16)
        self.save_excel = QtGui.QPushButton(self.layoutWidget6)
        self.save_excel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_excel.setFont(font)
        self.save_excel.setObjectName(_fromUtf8("save_excel"))
        self.horizontalLayout_16.addWidget(self.save_excel)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.dep_edit = QtGui.QPushButton(self.centralwidget)
        self.dep_edit.setGeometry(QtCore.QRect(1063, 13, 50, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dep_edit.sizePolicy().hasHeightForWidth())
        self.dep_edit.setSizePolicy(sizePolicy)
        self.dep_edit.setMinimumSize(QtCore.QSize(0, 20))
        self.dep_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(9)
        self.dep_edit.setFont(font)
        self.dep_edit.setObjectName(_fromUtf8("dep_edit"))
        self.dep_line = QtGui.QComboBox(self.centralwidget)
        self.dep_line.setEnabled(False)
        self.dep_line.setGeometry(QtCore.QRect(857, 13, 200, 23))
        self.dep_line.setMinimumSize(QtCore.QSize(200, 20))
        self.dep_line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dep_line.setEditable(False)
        self.dep_line.setObjectName(_fromUtf8("dep_line"))
        self.dep_line.addItem(_fromUtf8(""))
        self.dep_line.addItem(_fromUtf8(""))
        self.dep_line.addItem(_fromUtf8(""))
        self.dep_line.addItem(_fromUtf8(""))
        self.dep_line.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.label_32.setText(_translate("MainWindow", "项目列表", None))
        self.delete_2.setText(_translate("MainWindow", "删除项目", None))
        self.label_tables.setText(_translate("MainWindow", "项目详情", None))
        self.btn_add_project.setText(_translate("MainWindow", "新增项目", None))
        self.btn_add_subproject.setText(_translate("MainWindow", "新增展项", None))
        self.btn_add_task.setText(_translate("MainWindow", "新增任务", None))
        self.table_prodetail.setSortingEnabled(True)
        self.btn_exportExcel.setText(_translate("MainWindow", "导出Excel", None))
        self.btn_save.setText(_translate("MainWindow", "保存修改", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "详细信息", None))
        self.label_3.setText(_translate("MainWindow", "显示周期", None))
        self.schedual_method_combo.setItemText(0, _translate("MainWindow", "月", None))
        self.schedual_method_combo.setItemText(1, _translate("MainWindow", "周", None))
        self.schedual_method_combo.setItemText(2, _translate("MainWindow", "日", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "计划进度", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "项目管理", None))
        self.label_9.setText(_translate("MainWindow", "成员列表", None))
        self.label_17.setText(_translate("MainWindow", "姓名", None))
        self.label_18.setText(_translate("MainWindow", "职务", None))
        self.add_member_btn.setText(_translate("MainWindow", "添加成员", None))
        self.delete_member_btn.setText(_translate("MainWindow", "删除成员", None))
        self.label.setText(_translate("MainWindow", "已分配任务", None))
        self.label_12.setText(_translate("MainWindow", "日常", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "成员管理", None))
        self.label_2.setText(_translate("MainWindow", "查询成员", None))
        self.query_member.setItemText(0, _translate("MainWindow", "*", None))
        self.label_5.setText(_translate("MainWindow", "从", None))
        self.query_fromdate.setDisplayFormat(_translate("MainWindow", "yyyy-M-d", None))
        self.label_6.setText(_translate("MainWindow", "至", None))
        self.query_todate.setDisplayFormat(_translate("MainWindow", "yyyy-M-d", None))
        self.label_7.setText(_translate("MainWindow", "查询项目", None))
        self.query_project.setItemText(0, _translate("MainWindow", "*", None))
        self.label_13.setText(_translate("MainWindow", "查询展项", None))
        self.query_subproject.setItemText(0, _translate("MainWindow", "*", None))
        self.query.setText(_translate("MainWindow", "开始查询", None))
        self.query_overtime_table.setSortingEnabled(True)
        self.save_excel.setText(_translate("MainWindow", "保存到Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "加班统计", None))
        self.dep_edit.setText(_translate("MainWindow", "更改", None))
        self.dep_line.setItemText(0, _translate("MainWindow", "三维动画", None))
        self.dep_line.setItemText(1, _translate("MainWindow", "投标动画", None))
        self.dep_line.setItemText(2, _translate("MainWindow", "二维动画", None))
        self.dep_line.setItemText(3, _translate("MainWindow", "平面设计", None))
        self.dep_line.setItemText(4, _translate("MainWindow", "编导", None))

