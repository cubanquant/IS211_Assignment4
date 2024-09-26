import time
import random
import matplotlib.pyplot as plt

# Sequential Search
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

# Ordered Sequential Search
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

# Iterative Binary Search
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

# Recursive Binary Search
def binary_search_recursive(alist, item):
    start_time = time.time()
    
    def binary_search_helper(alist, item, first, last):
        if first > last:
            return False
        else:
            midpoint = (first + last) // 2
            if alist[midpoint] == item:
                return True
            else:
                if item < alist[midpoint]:
                    return binary_search_helper(alist, item, first, midpoint - 1)
                else:
                    return binary_search_helper(alist, item, midpoint + 1, last)
    
    found = binary_search_helper(alist, item, 0, len(alist) - 1)
    end_time = time.time()
    return found, end_time - start_time

# Main function to test the search algorithms and plot the results
def main():
    sizes = [500, 1000, 5000]
    num_tests = 100
    search_item = 99999999

    sequential_times = {size: [] for size in sizes}
    ordered_sequential_times = {size: [] for size in sizes}
    binary_iterative_times = {size: [] for size in sizes}
    binary_recursive_times = {size: [] for size in sizes}

    for size in sizes:
        for _ in range(num_tests):
            alist = [random.randint(1, 100000) for _ in range(size)]
            sorted_list = sorted(alist)

            _, time_taken = sequential_search(alist, search_item)
            sequential_times[size].append(time_taken)

            _, time_taken = ordered_sequential_search(sorted_list, search_item)
            ordered_sequential_times[size].append(time_taken)

            _, time_taken = binary_search_iterative(sorted_list, search_item)
            binary_iterative_times[size].append(time_taken)

            _, time_taken = binary_search_recursive(sorted_list, search_item)
            binary_recursive_times[size].append(time_taken)

    # Calculate average times
    avg_sequential_times = [sum(sequential_times[size]) / num_tests for size in sizes]
    avg_ordered_sequential_times = [sum(ordered_sequential_times[size]) / num_tests for size in sizes]
    avg_binary_iterative_times = [sum(binary_iterative_times[size]) / num_tests for size in sizes]
    avg_binary_recursive_times = [sum(binary_recursive_times[size]) / num_tests for size in sizes]

    # Print average times
    for size in sizes:
        print(f"Sequential Search took {avg_sequential_times[sizes.index(size)]:10.7f} seconds to run, on average for size {size}")
        print(f"Ordered Sequential Search took {avg_ordered_sequential_times[sizes.index(size)]:10.7f} seconds to run, on average for size {size}")
        print(f"Iterative Binary Search took {avg_binary_iterative_times[sizes.index(size)]:10.7f} seconds to run, on average for size {size}")
        print(f"Recursive Binary Search took {avg_binary_recursive_times[sizes.index(size)]:10.7f} seconds to run, on average for size {size}")
        print("\n" + "="*50 + "\n")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, avg_sequential_times, label='Sequential Search')
    plt.plot(sizes, avg_ordered_sequential_times, label='Ordered Sequential Search')
    plt.plot(sizes, avg_binary_iterative_times, label='Iterative Binary Search')
    plt.plot(sizes, avg_binary_recursive_times, label='Recursive Binary Search')
    plt.xlabel('List Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Average Search Time for Different Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()