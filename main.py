from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore


from ui_systemFrame import Ui_MainWindow as systemframe 

from tinydb import TinyDB

import sys
import time
import random
import platform,socket,re,uuid,psutil,logging
import speedtest


cpuPrevious = 0
cpucount = 0


class SystemScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = systemframe()
        self.ui.setupUi(self)



        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.ui.CloseButton.clicked.connect(self.closer)
        self.ui.Maximizebtn.clicked.connect(self.maxi)
        self.ui.Minimizebtn.clicked.connect(self.mini)
     
        self.opacity_effect = QGraphicsOpacityEffect()
        self.ui.CentralFrameBase.setGraphicsEffect(self.opacity_effect.setOpacity(1))

        
        allinfo = platform.uname()
        
        def getSystemInfo():
            try:
                info={}
                info['platform']=platform.system()
                info['platform-release']=platform.release()
                info['platform-version']=platform.version()
                info['architecture']=platform.machine()
                info['hostname']=socket.gethostname()
                info['ip-address']=socket.gethostbyname(socket.gethostname())
                info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
                info['processor']=platform.processor()
                info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
                
            except Exception as e:
                logging.exception(e)
            return info
        
        info = getSystemInfo()
        
        systemInformation = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" />
        <title>System Information</title><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:'Lucida Fax'; 
        font-size:10pt; font-weight:400; font-style:Lucida Fax;">\n<p style=" margin-top:0px; 
        margin-bottom:0px; margin-left:0px; margin-right:0px;
        -qt-block-indent:0; text-indent:0px;
        ">.<span style=" text-decoration: underline;">Platform</span>        - {SystemAndNo}</p>
        \n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
        margin-right:0px; -qt-block-indent:0; text-indent:0px;
        ">.<span style=" text-decoration: underline;">Version</span> 	      - {systemversion}</p>\n
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; 
        margin-right:0px; -qt-block-indent:0; text-indent:0px;">.<span style=" text-decoration: underline;">Architecture</span>  - {architecture}</p>
        \n<p style=" margin-top:0px; margin-bottom:0px; 
        margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">.<span style=" text-decoration: underline;">Processor</span>       - {processor}</p>
        \n<br><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; 
        margin-right:0px; -qt-block-indent:0; text-indent:0px;">.<span style=" text-decoration: underline;">HostName</span>      - {hostname}</p>
        \n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;
        -qt-block-indent:0; text-indent:0px;
        ">.<span style=" text-decoration: underline;">Ip Address </span>    - {ipadd}</p>
        \n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; 
        margin-right:0px; -qt-block-indent:0; text-indent:0px;">.<span style=" text-decoration: underline;">RAM (total) </span>    - {ram}</p>
        \n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; 
        text-indent:0px;">.<span style=" text-decoration: underline;">MAC Add.</span>       - {mcaddress} </p>
        \n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;
        -qt-block-indent:0; text-indent:0px;">.<span style=" text-decoration: underline;">PC Name  </span>      - {nodename}</p></body></html> 
        '''.replace('{SystemAndNo}',f"{allinfo.system} {allinfo.release} ").replace('{systemversion}',f'{allinfo.version}').replace('{architecture}',
        str(info['architecture'])).replace('{processor}',info['processor']).replace('{hostname}',info['hostname']).replace('{ipadd}',
        str(info['ip-address'])).replace('{ram}',info['ram']).replace('{mcaddress}',info["mac-address"]).replace('{nodename}',allinfo.node)


        def moveWindow(e):
            FRAME = QApplication.desktop().screenGeometry()
            if not (FRAME == self.geometry()):
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                    
        self.ui.TitleBar_2.mouseMoveEvent = moveWindow 
        self.oldgeo = self.geometry()   
        self.ui.systemInformation.setText(systemInformation)
        
        
        # self.cpusetter(75,self.ui.CPU)
        self.setMouseTracking(True)
        self.show()

        self.setvalue(0,self.ui.CPU,self.ui.CPUpercent)
        self.setvalue(0,self.ui.RAM,self.ui.RAMpercent)
        self.setvalue(0,self.ui.SWAP,self.ui.SwapPercent)



        self.processStart()
        
        # Testing all the circular bars
        # self.setvalue(75,self.ui.CPU,self.ui.CPUpercent)
        # self.setvalue(48,self.ui.RAM,self.ui.RAMpercent)
        # self.setvalue(63,self.ui.SWAP,self.ui.SwapPercent)
        
    
    def netspeed(self):
        speed = speedtest.Speedtest()
        for i in [0]:
            QApplication.processEvents()
            upload = speed.upload()
            download = speed.download()
        
        #_____________________________SEtting Values on the screen____________________
        self.ui.downloadSpeed.setText("{val2:.2f} Mb/s".format(val2=download/(10**7)))
        self.ui.UploadSpeed.setText("{val:.2f} Mb/s".format(val=upload/(10**7)))
    
    def netspeedupdate(self,tup_val):
        upload = tup_val[0]
        download = tup_val[1]
        self.ui.uploadSpeed.setText('{value:.2f}'.format(value=upload/(10**7)))
        self.ui.downloadSpeed.setText('{value:.2f}'.format(value=download/(10**7)))
        
    def processStart(self):
        edrive = psutil.disk_usage('/home')
        cdrive = psutil.disk_usage('/')
            
        eused = (90/100)* ( (edrive.used/edrive.total)*100)
        cused  = (90/100)* ( (cdrive.used/cdrive.total)*100)
            
        self.animation = QPropertyAnimation(self.ui.ddrivebar,b'value')
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(eused)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutBounce)
        self.animation.start()
            
        self.animation2 = QPropertyAnimation(self.ui.cdrivebar,b'value')
        self.animation2.setDuration(1000)
        self.animation2.setStartValue(1)
        self.animation2.setEndValue(cused)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutBounce)
        self.animation2.start()






        while True:
            QApplication.processEvents()
            ram = psutil.virtual_memory().percent
            swap = psutil.swap_memory().percent
            cpu = psutil.cpu_percent()


            
            edrive = psutil.disk_usage('/home')
            cdrive = psutil.disk_usage('/usr/bin')
            
            # eused = (90/100)* ( (edrive.used/edrive.total)*100)
            # cused  = (90/100)* ( (cdrive.used/cdrive.total)*100)
        
            eused = ( (edrive.used/edrive.total)*100)
            cused  =( (cdrive.used/cdrive.total)*100)
            
            #print("for E://",eused)

            if not self.hasFocus():   # If focus is lost then the window will becom semi transparent
                self.setWindowOpacity(0.5)
            else:
                self.setWindowOpacity(1)


            global cpuPrevious
            global cpucount
            globals()['cpuPrevious'] += cpu

            if cpucount == 15:
                self.setvalue(cpuPrevious/cpucount, self.ui.CPU, self.ui.CPUpercent)
                globals()['cpucount'] = 0
                globals()['cpuPrevious'] = 0


            self.setvalue(ram ,self.ui.RAM,self.ui.RAMpercent)
            self.setvalue(swap,self.ui.SWAP,self.ui.SwapPercent)
            
         
            self.ui.cdrivebar.setValue(cused)
            self.ui.ddrivebar.setValue(eused)

            globals()['cpucount'] += 1

            # #print('mousetracking',self.hasMouseTracking())



            #print('mouse track', self.hasMouseTracking())


    
    def mousePressEvent(self, event) -> None:
        self.clickPosition = event.globalPos()

    def fade(self):
        self.setWindowOpacity(0.4)
        QTimer.singleShot(1000,self.unfade)

    def unfade(self):
        self.setWindowOpacity(1)


    def setvalue(self, value,object,percentlabel):
            style = '''
        QFrame{
    border-radius: 124px;
    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1} rgba(31, 244, 75, 239), stop:{STOP2} rgba(0, 0, 0, 89));
    }'''
            # percent = '''
            # <html><head/><body><p align="center"><span style=" font-size:72pt; font-weight:600;">{PERCENT}</span><span style=" font-size:24pt;
            # font-weight:600; vertical-align:super;">%</span></p></body></html>
            # '''
            #
            percent = ''' 
            <html><head/><body><p align="center"><span style=" font-size:48pt; font-weight:600;">{PERCENT}</span>
            <span style=" font-size:24pt; font-weight:600; vertical-align:super;">%</span></p></body></html>
            '''

            progress = (100 - value) / 100
            stop_1 = progress
            stop_2 = progress - 0.001

            object.setStyleSheet(
                style.replace('{STOP1}', str(stop_1)).replace('{STOP2}', str(stop_2)))

            # loop = QEventLoop()
            # QTimer.singleShot(100, loop.quit)  # These three lines act like time.sleep(0.7)
            # loop.exec_()



            percentlabel.setText(percent.replace("{PERCENT}",'{value:.1f}'.format(value = value)))
            




    def closer(self):
        self.close()
        quit()
        
    def mini(self):
        self.showMinimized()
        
    def maxi(self):
        fullscreen = QApplication.desktop().screenGeometry() == self.geometry()

        if fullscreen:
            self.setGeometry(self.oldgeo)
        else:
            self.setGeometry(QApplication.desktop().screenGeometry())




        
if __name__ == '__main__':
    app = QApplication()
    window = SystemScreen()
    sys.exit(app.exec_())
    