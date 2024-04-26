import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QLineEdit


form_class = uic.loadUiType("pyqt02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self) :
        a = self.le.text()
        aa = int(a)
        aa -= 1
        
        self.le.setText(str(aa))

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()