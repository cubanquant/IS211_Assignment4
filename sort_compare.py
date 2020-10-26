import argparse
# other imports go here

import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = range(n)
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    pass


def shell_sort(a_list):
    pass


def python_sort(a_list):
    pass

if __name__ == "__main__":
    """Main entry point"""
    pass
