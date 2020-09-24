import concurrent.futures
import time


def do_something(seconds):
    time.sleep(seconds)
    print("done... {0}s".format(seconds))
    return seconds

# run processes with process pool
def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        result1 = executor.submit(do_something, 2)
        result2 = executor.submit(do_something, 3)
        
        # getting values as they complate
        for f in concurrent.futures.as_completed([result1, result2]):
            print(f.result())
        
        # or getting at the end
        print(result1.result(), result2.result())



# using map for pools
def main2():
    seconds = [5, 4, 3, 2, 1]

    # this done in 15 second 
    for sec in seconds:
        do_something(sec)

    # same example with process pool 
    # this done in 5 seconds
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(do_something, seconds)

        



# on windows we have to use __main__
#  https://stackoverflow.com/questions/14175348/why-does-pythons-multiprocessing-module-import-main-when-starting-a-new-pro
if __name__ == '__main__':
    main()
    main2()