#!/usr/bin/python

#Add my decorator to this 
def mydecorator(foo):
    def inner():
        print("Inside Inner in my decoratar")
        foo()
    return inner

def myfunc(x):
    print("Inside my func ", x)


# You can decorate a function without using the @ symbol
# Wrap the function with an inner function and then call it explicitly

def myouter(foo):
    
    def inner(x):
        print("Inside Inner in myouter func")
        foo(x)
    return inner

getfunc = myouter(myfunc)
getfunc(1)

def timestamp():
    import time
    import datetime
    ts = time.time()
    mask = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(ts).strftime(mask)


def add_time_stamp(foo):
    ''' add_time_stamp is a decorator accepting a function #foo '''
    def inner(*args, **kargs):
    #''' inner is the function containing the decoration which in this case consists of printing the timestamp and the calling the outer function '''
        print("Right before timestamp call")
        #foo(*args, **kargs)
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
    return 1

     

