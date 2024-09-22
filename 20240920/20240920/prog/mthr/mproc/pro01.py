import multiprocessing
import os
import time
def print_numbers():
    pid=os.getpid()
    for i in range(20):    
        print(f'{i}@{pid}')
        time.sleep(0.025)


if __name__ == '__main__':
    processes=[]
    process = multiprocessing.Process(target=print_numbers)
    processes.append(process)
    process.start()
    
  
    #process.join()
    print_numbers()
    
