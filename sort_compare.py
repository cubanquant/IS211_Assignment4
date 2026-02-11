import argparse
# other imports go here

import random
import time

# creating sorting functions

def insertion_sort(n):
    start = time.perf_counter()
    for index in range(1, len(n)):
        current_value = n[index]
        position = index

        while position > 0 and n[position - 1] > current_value:
            n[position] = n[position - 1]
            position = position - 1

        n[position] = current_value
    end = time.perf_counter()
    return n, end - start

def shell_sort(n):
    start = time.perf_counter()
    sublist_count = len(n) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(n, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.perf_counter()
    return n, end - start

def gap_insertion_sort(n, start, gap):
    for i in range(start + gap, len(n), gap):
        current_value = n[i]
        position = i

        while position >= gap and n[position - gap] > current_value:
            n[position] = n[position - gap]
            position = position - gap

        n[position] = current_value

def python_sort(n):
    start = time.perf_counter()
    n.sort()
    end = time.perf_counter()
    return n, end - start

# have to create parse function

def parse_args():
    parser = argparse.ArgumentParser(description="Benchmarking sort comparison")
    parser.add_argument(
        "--sizes", nargs="+", type=int, default=[500, 1000, 5000],
        help="The size of each sort comparison list"
    )
    parser.add_argument(
        "--runs", type=int, default=100,
        help="The number of runs per size of the list"
    )
    return parser.parse_args()

# creating main function

def main():
    args = parse_args()
    sizes = args.sizes
    number_of_runs = args.runs

    for size in sizes:
        times = {
            'insertion': 0,
            'shell': 0,
            'python': 0
        }

        for _ in range(number_of_runs):
            n = [random.randint(1, 10000) for _ in range(size)]

            _, t = insertion_sort(n[:])
            times['insertion'] += t

            _, t = shell_sort(n[:])
            times['shell'] += t

            _, t = python_sort(n[:])
            times['python'] += t

    print(f"\nList size: {size}")
    print(f"Insertion Sort took {times['insertion'] / number_of_runs:10.7f} seconds to run, on average")
    print(f"Shell Sort took {times['shell'] / number_of_runs:10.7f} seconds to run, on average")
    print(f"Python Sort took {times['python'] / number_of_runs:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()