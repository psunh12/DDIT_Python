import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize, QMessageBox



form_class = uic.loadUiType("pyqt_omok10_3.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.arr2d = [
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0],
            [0,0,0,0,0  ,0,0,0,0,0]
        ]
        self.arr2b = []
        self.flag_bw = True
        self.flag_over = False
        self.setupUi(self)
        
        for i in range(10):
            line= []
            for j in range(10):
                imsi = QPushButton(self)
                imsi.setIcon(QtGui.QIcon('0.png'))
                imsi.setIconSize(QSize(40, 40))  
                imsi.setGeometry(40*j, 40*i, 40, 40) 
                imsi.clicked.connect(self.myclick)
                imsi.setToolTip("{},{}".format(i,j))
                line.append(imsi)
            self.arr2b.append(line)
        self.pb.clicked.connect(self.myreset)
        self.show()
        self.myrender()
        
    def myreset(self):
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j]=0
                
        self.myrender()
        self.flag_bw = True
        self.flag_over = False
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j]==0:
                    self.arr2b[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2d[i][j]==1:
                    self.arr2b[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2d[i][j]==2:
                    self.arr2b[i][j].setIcon(QtGui.QIcon('2.png'))
      
    def getDW(self,i,j,stone):
        ret = 0
        try:
            while True:
                i+=1
                if i<0:
                    return ret
                
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getUP(self,i,j,stone):
        ret = 0
        try:
            while True:
                i-=1
                if i<0:
                    return ret
                
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getLE(self,i,j,stone):
        ret = 0
        try:
            while True:
                j-=1
                if i<0:
                    return ret
                if j<0:
                    return ret
                
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getRI(self,i,j,stone):
        ret = 0
        try:
            while True:
                j+=1
                if i<0:
                    return ret
                if j<0:
                    return ret
                
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
        
    def getUR(self,i,j,stone):
        ret = 0
        try:
            while True:
                i-=1
                j+=1
                if i<0:
                    return ret
                if j<0:
                    return ret
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getUL(self,i,j,stone):
        ret = 0
        try:
            while True:
                i-=1
                j-=1
                if i<0:
                    return ret
                if j<0:
                    return ret
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
        
    def getDR(self,i,j,stone):
        ret = 0
        try:
            while True:
                i+=1
                j+=1
                if i<0:
                    return ret
                if j<0:
                    return ret
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getDL(self,i,j,stone):
        ret = 0
        try:
            while True:
                i+=1
                j-=1
                if i<0:
                    return ret
                if j<0:
                    return ret
                if self.arr2d[i][j] == stone:
                    ret += 1
                else :
                    return ret
        except:
            return ret
        

    def myclick(self) :
        if self.flag_over:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = arr_ij[0]
        j = arr_ij[1]
        ii = int(i)
        jj = int(j)
        
        if self.arr2d[ii][jj]>0:
            return
        
        stone = -1
        if self.flag_bw :
            self.arr2d[ii][jj]=1
            stone = 1
        else:
            self.arr2d[ii][jj]=2
            stone = 2
            
        up = self.getUP(ii,jj,stone)
        dw = self.getDW(ii,jj,stone)
        le = self.getLE(ii,jj,stone)
        ri = self.getRI(ii,jj,stone)
        
        ur = self.getUR(ii,jj,stone)
        ul = self.getUL(ii,jj,stone)
        dr = self.getDR(ii,jj,stone)
        dl = self.getDL(ii,jj,stone)
        
        d1 = up + dw + 1
        d2 = ul + dr + 1
        d3 = le + ri + 1
        d4 = dl + ur + 1
        
        self.myrender()
        
        if d1==5 or d2==5 or d3==5 or d4==5:
            if self.flag_bw:
                QMessageBox.about(self,'오목','흑돌승리예유~이이')
            else:
                QMessageBox.about(self,'오목','백돌승리예유~이이')
            self.flag_over = True
        
        
        
        self.flag_bw = not self.flag_bw


        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()