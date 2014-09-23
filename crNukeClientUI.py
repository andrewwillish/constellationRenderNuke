#Constellation Render Manager Nuke v1.0
#Andrew Willis 2014

#Renderer Module

from PyQt4 import QtCore, QtGui
import socket, datetime, os, shutil, sys, time
from threading import Thread
import subprocess

USERNAMEvar=socket.gethostname()
DATE=datetime.datetime.now()

#Determining root path
rootPathVar=os.path.dirname(os.path.realpath(__file__)).replace('\\','/')

#change this to local working location
SERVERLOCvar=rootPathVar

CONSOLERETvar=''
RENSTATvar='VAC'
EXITCOMvar=0

class Ui_NUKEWATCHERfrm(QtGui.QWidget):
    def setupUi(self):
        CONSOLERETvar=''
        self.setObjectName("NUKEWATCHERfrm")
        self.setFixedSize(500, 31)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 100, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 83, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 44, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 100, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 83, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 44, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 100, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 83, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 44, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 33, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.setPalette(palette)
        self.STOPbtn = QtGui.QPushButton(self)
        self.STOPbtn.setGeometry(QtCore.QRect(0, 0, 500, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(157, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.STOPbtn.setPalette(palette)
        self.STOPbtn.setAutoFillBackground(True)
        self.STOPbtn.setFlat(True)
        self.STOPbtn.setObjectName("STOPbtn")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 67, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self._want_to_close = False
        self.show()
        
        #ADDITIONAL====================================================================================================

        THREAD1var=Thread(target=self.CHECKERfn,args=('a',))
        THREAD1var.start() 
        
        self.STOPbtn.clicked.connect(self.EXITfn)

        OPENSTATvar=open(SERVERLOCvar+'/data/clients/'+USERNAMEvar+'.clt','w')
        OPENSTATvar.close()

        #ADDITIONAL====================================================================================================
        return
    
    def EXITfn(self):
        global RENSTATvar, EXITCOMvar
        if RENSTATvar=='REN':
            EXITCOMvar=1
            self.STOPbtn.setEnabled(0)
            self.STOPbtn.setText('WAITING FOR RENDER THREAD TO FINISH')
        elif RENSTATvar=='VAC':
            try:
                os.remove(SERVERLOCvar+'/data/clients/'+USERNAMEvar+'.clt')
            except:
                pass
            sys.exit()
        return

    def CHECKERfn(self,NAMEvar):
        global EXITCOMvar
        while True:
            OPENSTATvar=open(SERVERLOCvar+'/data/clients/'+USERNAMEvar+'.clt','w')
            OPENSTATvar.close()
            JOBlis=os.listdir(SERVERLOCvar+'/data/jobs/1queue')
            if JOBlis<>[]:
                try:
                    self.RENDERfn()
                except Exception as err:
                    pass
            else:
                time.sleep(5)

            if EXITCOMvar==1:
                try:
                    os.remove(SERVERLOCvar+'/data/clients/'+USERNAMEvar+'.clt')
                except:
                    pass
                os._exit(0)
        return   
    
    def RENDERfn(self):
        global CONSOLERETvar, RENSTATvar

        #GET HOLD CHECK=================================================================================================
        OPENvar=open(SERVERLOCvar+'/data/hld.ini','r')
        READvar=OPENvar.readlines()
        OPENvar.close()

        HOLDlis=[]
        for chk in READvar:
            HOLDlis.append(chk.replace('\n',''))
        #GET HOLD CHECK=================================================================================================


        #PRE-RENDER=====================================================================================================
        JOBROOTvar=os.listdir(SERVERLOCvar+'/data/jobs/1queue')
        JOBROOTvar.sort()
        #Take out HOLD==================================================================================================
        for chk in HOLDlis:
            if chk in JOBROOTvar:
                JOBROOTvar.remove(chk)
        #Take out HOLD==================================================================================================

        if JOBROOTvar==[]:
            RENSTATvar='VAC'
            raise StandardError , 'error: empty job list'

        JOBROOTvar=JOBROOTvar[0]

        JOBvar=os.listdir(SERVERLOCvar+'/data/jobs/1queue/'+JOBROOTvar)
        
        JOBvar.sort()
        JOBvar=JOBvar[0]

        RENSTATvar='REN'

        #Write status to server=========================================================================================
        OPENSTATvar=open(SERVERLOCvar+'/data/clients/'+USERNAMEvar+'.clt','w')
        OPENSTATvar.write(JOBvar)
        OPENSTATvar.close()
        #Write status to server=========================================================================================

        if os.path.isdir(SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar)==False:
            os.mkdir(SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar)
            
        shutil.move(SERVERLOCvar+'/data/jobs/1queue/'+JOBROOTvar+'/'+JOBvar,SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar+'/'+JOBvar)
        if os.listdir(SERVERLOCvar+'/data/jobs/1queue/'+JOBROOTvar)==[]:
            os.rmdir(SERVERLOCvar+'/data/jobs/1queue/'+JOBROOTvar)
            
        OPENvar=open(SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar+'/'+JOBvar,'r')
        READvar=OPENvar.readlines()
        OPENvar.close()
        
        OUTPUTSTRvar=READvar[1]
        OUTPUTSTRvar=OUTPUTSTRvar[:OUTPUTSTRvar.rfind('/')]
        if os.path.isdir(OUTPUTSTRvar)==False:
            os.mkdir(OUTPUTSTRvar)
        #PRE-RENDER=====================================================================================================

        #RENDER=========================================================================================================
        TIMEOUTvar=0
        while True:
            if TIMEOUTvar==3:
                break
            #Render procedure
            #print 'RENDER FAIL SCENARIO'
            #time.sleep(5)
            subprocess.call(READvar[0],shell=True)
            #Render procedure

            #Render Confirmation Check
            FRAMERANGEvar=READvar[0][READvar[0].find('-F')+2:READvar[0].find('x1')]
            STARTvar=FRAMERANGEvar[:FRAMERANGEvar.find('-')]
            ENDvar=FRAMERANGEvar[FRAMERANGEvar.find('-')+1:]

            nameRoot=READvar[1]
            nameRoot=nameRoot[nameRoot.rfind('/')+1:nameRoot.find('%')]
            pathRoot=READvar[1][:READvar[1].rfind('/')+1]
            OUTPUTlis=os.listdir(pathRoot)


            #Render Confirmation Check
            OKlis=[]
            for chk in range(int(STARTvar),int(ENDvar)+1):
                if len(str(chk))==1:
                    chk='000'+str(chk)
                elif len(str(chk))==2:
                    chk='00'+str(chk)
                elif len(str(chk))==3:
                    chk='0'+str(chk)

                if nameRoot+str(chk)+'.png' in OUTPUTlis:
                    OKlis.append('PASS')
                else:
                    OKlis.append('FAIL')

            if 'FAIL' not in OKlis:
                break
            else:
                print '[RENDER FAILURE RE-RENDER LAST JOB]'
                TIMEOUTvar+=1
        #RENDER=========================================================================================================
        
        #POST-RENDER====================================================================================================
        #Write status to server=======================
        OPENSTATvar=open(SERVERLOCvar+'/data/clients/'+USERNAMEvar+'.clt','w')
        OPENSTATvar.write('COOLDOWN')
        OPENSTATvar.close()
        #Write status to server=======================

        if os.path.isdir(SERVERLOCvar+'/data/jobs/3done/'+JOBROOTvar)==False:
            os.mkdir(SERVERLOCvar+'/data/jobs/3done/'+JOBROOTvar)
        shutil.move(SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar+'/'+JOBvar,SERVERLOCvar+'/data/jobs/3done/'+JOBROOTvar+'/'+JOBvar)
        if os.listdir(SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar)==[]:
            os.rmdir(SERVERLOCvar+'/data/jobs/2wip/'+JOBROOTvar)

        time.sleep(10)
        RENSTATvar='VAC'
        #POST-RENDER====================================================================================================

        return 

    def __init__(self):
        super(Ui_NUKEWATCHERfrm,self).__init__()
        self.setupUi()
        return
    
    def closeEvent(self, evnt):
        if self._want_to_close:
            super(MyDialog, self).closeEvent(evnt)
        else:
            evnt.ignore()
            self.setWindowState(QtCore.Qt.WindowMinimized)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("NUKEWATCHERfrm", "Constellation Render Nuke Client ["+USERNAMEvar+"]", None, QtGui.QApplication.UnicodeUTF8))
        self.STOPbtn.setText(QtGui.QApplication.translate("NUKEWATCHERfrm", "STOP NUKE BATCH RENDERER", None, QtGui.QApplication.UnicodeUTF8))
        return
  
if __name__=='__main__':
    import sys
    app=QtGui.QApplication(sys.argv)
    ui=Ui_NUKEWATCHERfrm()
    sys.exit(app.exec_())