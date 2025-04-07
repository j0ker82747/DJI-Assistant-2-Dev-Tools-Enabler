import os,requests
from colorama import *
import hashlib
os.system('cls')


APP_ASAR_PATH = 'C:\\Program Files (x86)\\DJI Product\\DJI Assistant 2 (Consumer Drones Series)\\DJIApp\\app.asar'



def patch():
    enable_dev_tools_old = b'// mainWindow.webContents.openDevTools()'
    enable_dev_tools_new = b'mainWindow.webContents.openDevTools()   '

    anti_close_old = b'mainWindow.webContents.closeDevTools();'
    anti_close_new = b'                                       '

    no_args_old = b"let debug = process.argv[2]=='debug'?true:false"
    no_args_new = b"let debug = true                               "

    patch = open(APP_ASAR_PATH, 'rb').read().replace(no_args_old, no_args_new).replace(enable_dev_tools_old, enable_dev_tools_new).replace(anti_close_old, anti_close_new)

    file = open(APP_ASAR_PATH, 'wb')
    file.write(patch)
    file.close()

    print('    +--------------------+')
    print('   / Dev tools enabled! /')
    print('  +--------------------+')

    os.startfile(APP_ASAR_PATH.replace('\\DJIApp\\app.asar', '\\DJI Assistant 2.exe'))


def test():
    for filename in os.listdir('./src/build'):
        try:
            file = open('./src/build/{}'.format(filename), 'r', encoding='utf8').read()

            if 'enable-plugins' in file:
                print(filename)

        except:
             print('Passed due to error!')




if __name__ == '__main__':
    patch()      