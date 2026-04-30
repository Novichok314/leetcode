from threading import Semaphore

class Foo:
    def __init__(self):
        self.sem1 = Semaphore(0)
        self.sem2 = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.sem1.release()

    def second(self, printSecond):
        self.sem1.acquire()
        printSecond()
        self.sem2.release()

    def third(self, printThird):
        self.sem2.acquire()
        printThird()