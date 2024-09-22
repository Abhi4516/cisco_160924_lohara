import threading
import time
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(0.025)

threads=[]       
for i in range(5):   
      thread = threading.Thread(target=print_numbers)
      threads.append(i)
      thread.start()
  # Start the thread
#thread.join()   # Wait for the thread to finish

for i in range(10):
     thread.join()
print_numbers()

def print_numbers():
    thread_id = threading.get_ident()
    for i in range(5):
        print(f'@{thread_id}:{i}')
        time.sleep(1)



thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)
thread1.start()  # Start the thread
thread2.start()  # Start the thread
#thread1.join()   # Wait for the thread to finish
#thread2.join()   # Wait for the thread to finish
print_numbers() 