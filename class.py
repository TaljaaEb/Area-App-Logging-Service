#FIFO
RIGTING = "" #Reverse
ROLE = ""
BUFF = ""

from service import Service

class Order2Invoice(Service):

    def __init__(self):
        super(Order2Invoice, self).__init__()

class Invoice2Order(Service):

    def __init__(self):
        super(Order2Invoice, self).__init__()

class Buyer2Invoice(Service):

    def __init__(self):
        super(Order2Invoice, self).__init__()

class Seller2Invoice(Service):

    def __init__(self):
        super(Order2Invoice, self).__init__()

def substring():
    pass

#HD
from threading import Timer, Event
def gfg():
    print(BUFF)

timer = Timer(10.0, gfg)
timer.start()
