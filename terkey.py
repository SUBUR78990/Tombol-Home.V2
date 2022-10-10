
import os
from time import sleep
import socket,struct,time,os,sys

def tik():
    titik = [
     '   ', '.  ', '.', '..', '...', '...', ',', '[\033[1;32m\xe2\x9c\x93\033[1;37m]']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;96mPROSESS SEDANG MENG INSTALL  \x1b[1;97m'+o,
        sys.stdout.flush()
        time.sleep(0.9)
def looding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m\xe2\x9c\x93\033[0m]\n']
    
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mTUNGGU SAMBIL NGOPI \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.2)

def setup():
       try:
           os.mkdir('/data/data/com.termux/files/home/.termux')
       except:
           pass
       key = "extra-keys = [['ESC','/','HACKED','HOME','UP','login','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'],['KEYBOARD','','PEMBUAT','BY','SUBUR.M','','DRAWER']]"
       open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
       os.system('termux-reload-settings')

os.system('clear')
print """                                                             
 _|    _|    _|_|      _|_|_|  _|    _|  _|_|_|_|  _|_|_|    
 _|    _|  _|    _|  _|        _|  _|    _|        _|    _|  
 _|_|_|_|  _|_|_|_|  _|        _|_|      _|_|_|    _|    _|  
 _|    _|  _|    _|  _|        _|  _|    _|        _|    _|  
 _|    _|  _|    _|    _|_|_|  _|    _|  _|_|_|_|  _|_|_| """
print('')
ana = raw_input('\033[1;92mINI ADALAH TOOLS UNTUK MENAMPILKAN TOMBOL HOME [TERMUX] ANDA \033[31;1m\n\033[37;1mLANJUTKAN TEKAN ENTER \033[37;1m : ')
os.system('clear')
looding2()
print('')
tik()
setup()
os.system('clear')
wk = raw_input('\033[1;91mSELESAI [\033[32;1mCLOSE TEKAN \033[33;1m+ \033[32;1mENTER\033[37;1m]')
os.system('exit')

