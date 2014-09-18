import os

OUTPUTSTRvar='R:/KIKO/DIR_TEST/nukebutcher_test'

TEMPlis=[]
CHECKvar=''
for chk in OUTPUTSTRvar:
    if chk=='/':
        CHECKvar=CHECKvar+chk
        if os.path.isdir(CHECKvar)==False:
            os.mkdir(CHECKvar)
    else:
        CHECKvar=CHECKvar+chk
if os.path.isdir(OUTPUTSTRvar)==False:
    os.mkdir(OUTPUTSTRvar)