# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import ui_newDailyDialog

class newDailyDialog(ui_newDailyDialog.Ui_dialog):
    def __init__(self,parent=None):
        super(newDailyDialog,self).__init__(parent)
        self.setupUi(self)
        date = QDate.currentDate()
        self.dateEdit.setDate(date)
        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = newDailyDialog()
    dialog.show()
    app.exec_()


