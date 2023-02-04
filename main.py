import time

from module_1.foo import p1
from module_2.foo import p2
from module_3.foo import p3
from module_4.foo import p4


if __name__ == "__main__":
    while True:
        p1()
        p2()
        p3()
        p4()
        print("Finish execution once")
        time.sleep(5)