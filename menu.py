#GENERAL MENU HERE
import imp

#Determining root path
rootPathVar=os.path.dirname(os.path.realpath(__file__)).replace('\\','/')

def launcherscr(scr,srvrname):
    print srvrname
    print 'Calling >> ',scr

    print srvrname+scr+'.pyc'
    imp.load_compiled(scr,srvrname+'/'+scr+'.pyc')
    
    #exec('import '+scr) in globals()
    #exec('reload('+scr+')')in globals() 
    return

nuke.menu( 'Nuke' ).addCommand( 'crNuke/Submitter',lambda*args:launcherscr('crNukeSubmitterUI', rootPathVar))
nuke.menu( 'Nuke' ).addCommand( 'crNuke/Launch Controller',lambda*args:os.startfile(rootPathVar+'/crControllerLauncher.bat'))
nuke.menu( 'Nuke' ).addCommand( 'crNuke/Launch Renderer',lambda*args:os.startfile(rootPathVar+'/crClientLauncher.bat'))