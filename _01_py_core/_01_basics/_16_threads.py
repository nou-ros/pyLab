'''
Threads: An entity within a process that can be scheduled aka lightweight process. A process can spawn multiple threads. 

+ All threads within a process share the same memory.
+ Lightweight
+ Starting a thread is faster than starting a process.
+ Great for I/O-bound tasks.

- Threading is limited by GIL: Only one thread at a time.
- No effect for CPU-bound tasks
- Not interruptable/killable
- Careful with race conditions. (Race condition: when two or more threads wants to access the same resource)

GIL - Global interpreter lock
This is a mutex (or a lock) that allows only one thread to hold control of the Python interpreter. This means that the GIL allows only one thread to execute at a time even in 
a multi-threaded architecture.

Why is it needed?
It is needed because CPython's (reference implementation of Python) memory management is not thread-safe. Python uses reference counting for memory management. It means that 
bjects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory
occupied by the object is released. The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its 
value simultaneously. If this happens, it can cause either leaked memory that is never released or incorrectly release the memory while a reference to that object still exists.

How to avoid the GIL
The GIL is very controversial in the Python community. The main way to avoid the GIL is by using multiprocessing instead of threading. Another (however uncomfortable) solution
would be to avoid the CPython implementation and use a free-threaded Python implementation like Jython or IronPython. A third option is to move parts of the application out 
into binary extensions modules, i.e. use Python as a wrapper for third party libraries (e.g. in C/C++). This is the path taken by numypy and scipy.

When is Threading useful:
Despite the GIL it is useful for I/O-bound tasks when your program has to talk to slow devices, like a hard drive or a network connection. With threading the program can use
the time waiting for these devices and intelligently do other tasks in the meantime.
Example: Download website information from multiple sites. Use a thread for each site.

Working: 
- How to create and start multiple threads
- How to wait for threads to complete
- How to share data between threads
- How to use Locks to prevent race conditions
- What is a daemon thread
- How to use a Queue for thread-safe data/task processing.

Create and run threads
You create a thread with threading.Thread(). It takes two important arguments:

target: a callable object (function) for this thread to be invoked when the thread starts
args: the (function) arguments for the target function. This must be a tuple
Start a thread with thread.start()

Call thread.join() to tell the program that it should wait for this thread to complete before it continues with the rest of the code.'''

'''
# work with 2 threads.

import threading
import time 
start = time.perf_counter()
# starting single threads - 1
def do_something():
    print('Sleeping 1 second....')
    time.sleep(1)
    print('Done sleeping')
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join()
'''

# Note: The following example usually won't benefit from multiple threads since it is CPU-bound. It should just show the example of how to use threads.
from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()
        
'''       
# new way of doing multithreading

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print(f'Done sleeping {seconds}') with concurrent approach
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())
    
    # results = [executor.submit(do_something, 1) for _ in range(10)]

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    
    # for result in results:
    #     print(result)
    


# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')
'''

'''Share data between threads
Since threads live in the same memory space, they have access to the same (public) data. Thus, you can for example simply use a global variable to which all threads have 
read and write access.

Task: Create two threads, each thread should access the current database value, modify it (in this case only increase it by 1), and write the new value back into the database 
value. Each thread should do this operation 10 times.
'''

from threading import Thread
import time


# all threads can access this global variable
database_value = 0

def increase():
    global database_value # needed to modify the global value
    
    # get a local copy (simulate data retrieving)
    local_copy = database_value
        
    # simulate some modifying operation
    local_copy += 1
    time.sleep(0.1)
        
    # write the calculated new value into the global variable
    database_value = local_copy


if __name__ == "__main__":

    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')


'''How to use Locks
Notice that in the above example, the 2 threads should increment the value by 1, so 2 increment operations are performed. But why is the end value 1 and not 2?

Race condition
A race condition happened here. A race condition occurs when two or more threads can access shared data and they try to change it at the same time. Because the thread 
scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data. In our case, the first thread 
accesses the database_value (0) and stores it in a local copy. It then increments it (local_copy is now 1). With our time.sleep() function that just simulates some time 
consuming operations, the programm will swap to the second thread in the meantime. This will also retrieve the current database_value (still 0) and increment the local_copy 
to 1. Now both threads have a local copy with value 1, so both will write the 1 into the global database_value. This is why the end value is 1 and not 2.

Avoid race conditions with Locks
A lock (also known as mutex) is a synchronization mechanism for enforcing limits on access to a resource in an environment where there are many threads of execution. A Lock 
has two states: locked and unlocked. If the state is locked, it does not allow other concurrent threads to enter this code section until the state is unlocked again.

Two functions are important:

lock.acquire() : This will lock the state and block
lock.release() : This will unlock the state again.
Important: You should always release the block again after it was acquired!

In our example the critical code section where database values are retrieved and modified is now locked. This prevents the second thread from modyfing the global data at the 
same time. Not much has changed in our code. All new changes are commented in the code below.'''

# import Lock
from threading import Thread, Lock
import time


database_value = 0

def increase(lock):
    global database_value 
    
    # lock the state
    lock.acquire()
    
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    
    # unlock the state
    lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()
    
    print('Start value: ', database_value)

    # pass the lock to the target function
    t1 = Thread(target=increase, args=(lock,)) # notice the comma after lock since args must be a tuple
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')


'''Use the lock as a context manager
After lock.acquire() you should never forget to call lock.release() to unblock the code. You can also use a lock as a context manager, wich will safely lock and unlock your 
code. It is recommended to use a lock this way:'''

def increase(lock):
    global database_value 
    
    with lock: 
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


'''

Using Queues in Python
Queues can be used for thread-safe/process-safe data exchanges and data processing both in a multithreaded and a multiprocessing environment.

The queue
A queue is a linear data structure that follows the First In First Out (FIFO) principle. A good example is a queue of customers that are waiting in line, where the customer
that came first is served first.'''

from queue import Queue

# create queue
q = Queue()

# add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1 

# now q looks like this:
# back --> 3 2 1 --> front

# get and remove first element
first = q.get() # --> 1
print(first) 

# q looks like this:
# back --> 3 2 --> front

'''Using a queue in multithreading
Operations with a queue are thread-safe. Important methods are:

q.get() : Remove and return the first item. By default, it blocks until the item is available.
q.put(item) : Puts element at the end of the queue. By default, it blocks until a free slot is available.
q.task_done() : Indicate that a formerly enqueued task is complete. For each get() you should call this after you are done with your task for this item.
q.join() : Blocks until all items in the queue have been gotten and proccessed (task_done() has been called for each item).
q.empty() : Return True if the queue is empty.

The following example uses a queue to exchange numbers from 0...19. Each thread invokes the worker method. Inside the infinite loop the thread is waiting until items are 
available due to the blocking q.get() call. When items are available, they are processed (i.e. just printed here), and then q.task_done() tells the queue that processing is 
complete. In the main thread, 10 daemon threads are created. This means that they automatically die when the main thread dies, and thus the worker method and infinite loop is
no longer invoked. Then the queue is filled with items and the worker method can continue with available items. At the end q.join() is necessary to block the main thread until
all items have been gotten and proccessed.'''


from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')



'''Daemon threads
In the above example, daemon threads are used. Daemon threads are background threads that automatically die when the main program ends. This is why the infinite loops inside
the worker methods can be exited. Without a daemon process we would have to use a signalling mechanism such as a threading.Event to stop the worker. But be careful with 
daemon processes: They are abruptly stopped and their resources (e.g. open files or database transactions) may not be released/completed properly.'''
