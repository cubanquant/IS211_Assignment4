import argparse
import time
import random

# creating search functions

def sequential_search(n, item):
    start = time.perf_counter()
    for i in n:
        if i == item:
            end = time.perf_counter()
            return True, end - start
    end = time.perf_counter()
    return False, end - start

def ordered_sequential_search(n, item):
    n.sort()
    start = time.perf_counter()
    for i in n:
        if i == item:
            end = time.perf_counter()
            return True, end - start
        elif i > item:
            break
    end = time.perf_counter()
    return False, end - start

def binary_search_iterative(n, item):
    n.sort()
    start = time.perf_counter()
    first = 0
    last = len(n) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if n[midpoint] == item:
            found = True
        else:
            if item < n[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.perf_counter()
    return found, end - start


def binary_search_recursive(n, item):
    n.sort()
    start = time.perf_counter()
    result = binary_search_recursive_helper(n, item, 0, len(n) - 1)
    end = time.perf_counter()
    return result, end - start


def binary_search_recursive_helper(n, item, start_idx, end_idx):
    if start_idx == end_idx:
        return False
    mid = (start_idx + end_idx) // 2
    if n[mid] == item:
        return True
    elif item < n[mid]:
        return binary_search_recursive_helper(n, item, start_idx, mid - 1)
    else:
        return binary_search_recursive_helper(n, item, mid + 1, end_idx)

# have to create parse function

def parse_args():
    parser = argparse.ArgumentParser(description="Benchmarking search comparison")
    parser.add_argument(
        "--sizes", nargs="+", type=int, default=[500, 1000, 5000],
        help="The number of sizes to compare ex: (500, 1000, 5000)",
    )
    parser.add_argument(
        "--runs", nargs="+", type=int, default=100,
        help="The number of runs to compare (default: 100)",
    )
    return parser.parse_args()

# creating main function

def main():
    args = parse_args()
    sizes = args.sizes
    number_of_runs = args.runs
    target = 99999999

    for size in sizes:
        times = {
            'sequential': 0,
            'ordered': 0,
            'binary_iter': 0,
            'binary_rec': 0,
        }

        for _ in range(number_of_runs):
            n = [random.randint(1, 10000) for _ in range(size)]

            _, t = sequential_search(n[:], target)
            times['sequential'] += t

            _, t = ordered_sequential_search(n[:], target)
            times['ordered'] += t

            _, t = binary_search_iterative(n[:], target)
            times['binary_iter'] += t

            _, t = binary_search_recursive(n[:], target)
            times['binary_rec'] += t

    print(f"\nList size: {size}")
    print(f"Sequential Search took {times['sequential'] / number_of_runs:10.7f} seconds to run, on average")
    print(f"Ordered Sequential Search took {times['ordered'] / number_of_runs:10.7f} seconds to run, on average")
    print(f"Binary Search Iterative took {times['binary_iter'] / number_of_runs:10.7f} seconds to run, on average")
    print(f"Binary Search Recursive took {times['binary_rec'] / number_of_runs:10.7f} seconds, on average")

if __name__ == "_main_":
    main()