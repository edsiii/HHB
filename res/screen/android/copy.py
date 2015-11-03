import os
import shutil


for f in os.listdir('.'):
    if 'screen-' == f[:7]:
        _, res, orientation = f.split('-')
        orientation = 'land' if 'landscape.png' == orientation else 'port'
        df = '../../../../platforms/android/res/drawable-%s-%s/screen.png' % (orientation, res)
        print f, '=>', df
        shutil.copyfile(f, df)
