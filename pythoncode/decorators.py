#!/usr/bin/python

import os
import sys

def myfunc():
    print("This is inside myfunc")

def mydecorator():
    pass


def timestamp():
    import time
    import datetime
    ts = time.time()
    mask = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(ts).strftime(mask)


def add_time_stamp(foo):
    ''' add_time_stamp is a decorator accepting a function #foo '''
    def inner(*args, **kargs):
    ''' inner is the function containing the decoration which in this 
    case consists of printing the timestamp and the calling the outer function '''
        print(timestamp(),foo(*args, **kargs))
        
    return inner

@add_time_stamp
def show_msg(msg):
    '''
    show_msg takes a single parameter as its argument and prints
    it to the screen.
                 
     Note that the definition of show_msg is preceeded by @add_time_stamp
     something that is equivalent to the following:
                          
     def show_msg(msg): print msg
     show_msg = add_time_stamp(show_msg)
     '''
    print( msg)


if __name__=="__main__":
    show_msg('test')

