import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import scheduleWidget



class mainwidow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        
        self.setGeometry(100,100,1200,800)
        newwidget = scheduleWidget.scheduleWidget()
       
        self.setCentralWidget(newwidget)
        
        
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = mainwidow()
    window.show()
    app.exec_()