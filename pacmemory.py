#!/usr/bin/python3
from time import sleep
from os import system
from threading import Thread

def show_memory_usage():
    system("free")
    sleep(1)

thread = Thread(target=show_memory_usage)
thread.start()

memory = list()
while(True):
    memory.append("a")
