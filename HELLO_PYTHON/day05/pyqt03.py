import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QTextEdit


form_class = uic.loadUiType("pyqt03.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self) :
        dan = self.le.text()
        idan = int(dan)
        
        txt = ""
        
        for i in range(1,9+1):
            txt += "{}*{}={}\n".format(idan,i,idan*i)
        
        self.te.setText(txt)

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    
    
    