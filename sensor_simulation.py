#!/usr/bin/env python3
import random
import time

def read_sensor():
    # شبیه‌سازی دریافت داده از سنسور
    return round(random.uniform(20.0, 30.0), 2)

if __name__ == '__main__':
    for _ in range(10):
        print("سنسور خوانش:", read_sensor())
        time.sleep(1)
