import multiprocessing
import time


# ! in order to use a function with multiprocessing arguments MUST be pickle serializable 


def do_something(seconds):
    time.sleep(seconds)
    print("done...")


# simple multiprocess example
def main():
    m = multiprocessing.Process(target=do_something, args=[1.5])

    # start thread
    m.start()
    # ----
    # do stuff on main thread
    print("hi")
    # ----

    # join thread
    m.join()



# example with multiple processes
def main2():
    # create 10 processes
    processes = []
    for _ in range(10):
        m = multiprocessing.Process(target=do_something, args=[1.5])
        processes.append(m)

    # start processes
    for process in processes:
        process.start()
    
    # ----
    # do stuff on main processes
    print("hi")
    # ----

    # join processes
    for process in processes:
        process.join()




# on windows we have to use __main__
#  https://stackoverflow.com/questions/14175348/why-does-pythons-multiprocessing-module-import-main-when-starting-a-new-pro
if __name__ == '__main__':
    main()
    main2()

