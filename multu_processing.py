#  python multiprocessing  = running task inparrallel on diffrent cpu cores, bypassesGIL used for threading

# multi processing is better for cpu bound tasks(heavy cpu usage)
#multithreading is better for IO bound task (waiting around)


from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    a = Process(target=counter,args=(1000000000,))
    a.start()
    a.join()
    print("finished  in",time.perf_counter(),"seconds")

if __name__ == '__main__':
    main()
