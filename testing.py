from lib import delete_txt_files
delete_txt_files.run()

import threading
from lib import monitoring

from algo import algo1
from algo import algo2

import time

t = threading.Thread(target=monitoring.capture)
t.start()

t.status = 'idle'
time.sleep(.1)

t.status = 'algo1'
algo1.run()

t.status = 'idle'

t.status = 'algo2'
algo2.run()

t.status = 'idle'
time.sleep(.1)

t.running = False
