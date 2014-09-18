#NUKE BATCHER SUBMITTER

import nuke, datetime, os

import os, nuke, shutil, datetime

DATE=datetime.datetime.now()

SERVERvar='Y:/TECH/constellationRenderNuke'
NUKEDIRvar='C:\Program Files\Nuke7.0v5\Nuke7.0.exe'


class NUKEBATCHERSUBMITTERcls:
    def __init__(self):
        
        PANEL=nuke.Panel('Constellation Render Manager [NUKE]')
        PANEL.setWidth(350)
        
        #Select Write Node
        ALLNODElis=nuke.root().nodes()
        WRITElis=[]
        for chk in ALLNODElis:
            if str(chk.name()).find('Write')!=-1:
                WRITElis.append(chk.name())
        if len(WRITElis)>1:
            PANEL.addEnumerationPulldown('Select Write',str('" " '+' '.join(WRITElis)))
        PANEL.addEnumerationPulldown( 'Threads', '1 2 4 8' )
        PANEL.addSingleLineInput('Block Divider','10')
        PANEL.addSingleLineInput('Start Frame',nuke.root().firstFrame())
        PANEL.addSingleLineInput('End Frame',nuke.root().lastFrame())
        
        RET=PANEL.show()
        if RET==1:
            if len(WRITElis)>1:
                WRITEvar=PANEL.value('Select Write')
            else:
                try:
                    WRITEvar=WRITElis[0]
                except:
                    nuke.message('')
            self.SUBMITTERALGfn(WRITEvar,PANEL.value('Threads'),PANEL.value('Block Divider'), PANEL.value('Start Frame'), PANEL.value('End Frame'))
        return
    
    def SUBMITTERALGfn(self,WRITENODEvar, THREADvar, BLOCKDIVvar, STARTFRAMEvar, ENDFRAMEvar):
        TARGETFILEvar=str(nuke.root().name())
        #Submission procedure
        if WRITENODEvar==' ' or THREADvar==' ' or BLOCKDIVvar==' ' or STARTFRAMEvar==' ' or ENDFRAMEvar==' ':
            nuke.message('Incomplete information submission to NukeButcher render!')
            raise ValueError, '[NUKEBATCHER] - Incomplete submission information!'
        else:
            if BLOCKDIVvar.isdigit()==False:
                nuke.message('Invalid block divider input!')
                raise ValueError, '[NUKEBATCHER] - Invalid Block Divider Input'
            if STARTFRAMEvar.isdigit()==False:
                nuke.message('Invalid start frame input!')
                raise ValueError, '[NUKEBATCHER] - Invalid start frame Input'      
            if ENDFRAMEvar.isdigit()==False:
                nuke.message('Invalid end frame input!')
                raise ValueError, '[NUKEBATCHER] - Invalid end frame Input'     
            
            #Get Renderer Path
            RENDPATHvar=nuke.toNode(WRITENODEvar)['file'].value()
            RENDPATHvar=RENDPATHvar[:RENDPATHvar.rfind('/')]
                          
            #Submitting job
            #"C:\Program Files\Nuke7.0v4\Nuke7.0.exe" -i -X Write1 -m 8 -x C:\Users\andrew.willis\Desktop\testing001B.nk
            if ENDFRAMEvar<STARTFRAMEvar:
                raise ValueError, '[NUKEBATCHER] - Start frame is larger than End frame!'
            
            DATE=datetime.datetime.now()
            IDvar=str(DATE.year)+str(DATE.month)+str(DATE.day)+str(DATE.hour)+str(DATE.minute)+str(DATE.second)+str(DATE.microsecond)
            os.mkdir(SERVERvar+'/data/jobs/1queue/'+IDvar)
            
            RANGEvar=int(ENDFRAMEvar)-int(STARTFRAMEvar)
            cnb=1
            PROGRESSvar=int(STARTFRAMEvar)-1
            while RANGEvar>=0:
                if int(RANGEvar)<int(BLOCKDIVvar):
                    PROGRESSvar+=1
                    OPENvar=open(SERVERvar+'/data/jobs/1queue/'+IDvar+'/'+IDvar+'-'+str(cnb)+'.nbf','w')
                    OPENvar.write('"'+NUKEDIRvar+'" -i -X '+WRITENODEvar+' -m '+THREADvar+' -F'+str(PROGRESSvar)+'-'+str(int(PROGRESSvar)+int(RANGEvar))+'x1'+' -x '+TARGETFILEvar+'\n'+RENDPATHvar)
                    OPENvar.close()
                    PROGRESSvar=PROGRESSvar+RANGEvar
                else:
                    PROGRESSvar+=1
                    OPENvar=open(SERVERvar+'/data/jobs/1queue/'+IDvar+'/'+IDvar+'-'+str(cnb)+'.nbf','w')
                    OPENvar.write('"'+NUKEDIRvar+'" -i -X '+WRITENODEvar+' -m '+THREADvar+' -F'+str(PROGRESSvar)+'-'+str(int(PROGRESSvar)+int(BLOCKDIVvar))+'x1'+' -x '+TARGETFILEvar+'\n'+RENDPATHvar)
                    OPENvar.close() 
                    PROGRESSvar=int(PROGRESSvar)+int(BLOCKDIVvar)
                    
                RANGEvar-=int(BLOCKDIVvar)+1
                cnb+=1
            nuke.message('Job has been submitted for network rendering!')
            
        return

if nuke.root().name()=='Root':
    nuke.message('File has not been saved!')
    raise ValueError, 'File has not been saved!'
NUKEBATCHERSUBMITTERcls()