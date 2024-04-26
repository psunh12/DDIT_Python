import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPlainTextEdit


form_class = uic.loadUiType("pyqt07.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def getStar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "★"
        ret += "\n"
        return ret
        
    def myclick(self) :
        str_f = self.le_first.text()
        str_l = self.le_last.text()
        int_f = int(str_f)
        int_l = int(str_l)
        
        txt = ""
        for i in range(int_f,int_l+1):     
            txt += self.getStar(i)
        
        self.pte.setPlainText(txt)
        
        
        

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()