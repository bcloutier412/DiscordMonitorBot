import threading
from aquaHQ import aquaHQrun
from yuckPass import yuckPassrun

thread2 = threading.Thread(target=yuckPassrun)

thread1 = threading.Thread(target=aquaHQrun)
thread2.start()
thread1.start()

