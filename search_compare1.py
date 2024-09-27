import time
import random

def sequential_search(alist, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    end_time = time.time()
    return found, end_time - start_time

def ordered_sequential_search(alist, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    
    end_time = time.time()
    return found, end_time - start_time

def binary_search_iterative(alist, item):
    start_time = time.time()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    end_time = time.time()
    return found, end_time - start_time

def binary_search_recursive(alist, item):
    start_time = time.time()
    if len(alist) == 0:
        end_time = time.time()
        return False, end_time - start_time
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            end_time = time.time()
            return True, end_time - start_time
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint + 1:], item)

def main():
    list_sizes = [500, 1000, 5000]
    avg_times = {'Sequential Search': 0, 'Ordered Sequential Search': 0, 'Binary Search Iterative': 0, 'Binary Search Recursive': 0}

    for size in list_sizes:
        for _ in range(100):
            random_list = random.sample(range(1, 10000), size)
            random_list.sort()

            _, seq_time = sequential_search(random_list, 99999999)
            _, ord_seq_time = ordered_sequential_search(random_list, 99999999)
            _, bin_iter_time = binary_search_iterative(random_list, 99999999)
            _, bin_rec_time = binary_search_recursive(random_list, 99999999)

            avg_times['Sequential Search'] += seq_time
            avg_times['Ordered Sequential Search'] += ord_seq_time
            avg_times['Binary Search Iterative'] += bin_iter_time
            avg_times['Binary Search Recursive'] += bin_rec_time
    
    for algo, time_taken in avg_times.items():
        avg_time = time_taken / 100
        print(f"{algo} took {avg_time:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()
