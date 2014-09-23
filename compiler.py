try:
    import crNukeControllerUI
    reload (crNukeControllerUI)
except Exception as e:
    print str(e)
    pass

try:
    import crNukeClientUI
    reload (crNukeClientUI)
except:
    pass