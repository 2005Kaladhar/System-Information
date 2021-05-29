from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import random
import sys
import time

from ui_CircularProgressBar import Ui_MainWindow as circularbar


count = 0

class CircularProgressBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = circularbar()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        # self.setvalue(98)
        self.show()
        self.progresser()

    def progresser(self):
        global count


        while True:
            QApplication.processEvents()
            time.sleep(0.1)
            if count == 100:
                globals()['count'] = 0
            self.setvalue(count)
            globals()['count']+=1


    def setvalue(self,value):
        style = '''
    QFrame{
border-radius: 124px;
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1} rgba(31, 244, 75, 239), stop:{STOP2} rgba(0, 0, 0, 89));
}'''
        percent = '''
        <html><head/><body><p align="center"><span style=" font-size:72pt; font-weight:600;">{PERCENT}</span><span style=" font-size:24pt; 
        font-weight:600; vertical-align:super;">%</span></p></body></html>
        '''

        loadingLabel = '''
        <html><head/><body><p align="center"><span style=" font-size:11pt; 
        font-weight:600;"></span><span style=" font-size:11pt;">{LOAD}</span></p></body></html>
        '''
        progress = (100-value)/100
        stop_1 = progress
        stop_2 = progress-0.001

        loadingkeys = ['Loading','Searching',"Connecting","Getting",'Looking for']

        dots = count
        if count>=3:
            dots = 1

        self.ui.percentLabel.setText(percent.replace('{PERCENT}',str(count)))
        self.ui.CircularProgress.setStyleSheet(style.replace('{STOP1}',str(stop_1)).replace('{STOP2}',str(stop_2)))
        self.ui.loadingLabel.setText(loadingLabel.replace('{LOAD}',f'{random.choice(loadingkeys)}{"."*dots}  '))
if __name__ == '__main__':
    app = QApplication()
    window = CircularProgressBar()
    sys.exit(app.exec_())
    