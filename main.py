import random, time
import tabulate


def qsort(a, pivot_fn):
    ## TO DO
  if len(a) <= 1:
    return a
    #first_var = a
  else:
    pivot = pivot_fn(a) #defines our pivot variable
    left = list(filter(lambda x: x<pivot, a)) #used to sort the list about the pivot.
    center = list(filter(lambda x: x==pivot, a))#x in list is the pivot
    right = list(filter(lambda x: x>pivot, a))#x in list is bigger than pivot is right
    return qsort(left, pivot_fn) + center + qsort(right, pivot_fn)


#we could not figure out the implementation of ssort since it was not given to us
#this was the implementation given in the slides but it made an infinite loop
#sorry
#def ssort(L):
#    for i in range(len(L)):
#        print(L)
#        m = L.index(min(L[i:]))
#        L[i], L[m] = L[m], L[i]
#    return L
#sposed to be a call here w an array
#ssort_call = ssort([0])

def fix_pivot(a):
  return a[0]

def random_pivot(a):
  return random.choice(a)
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###
def random_var(x):#can be anything: in or out the list
  return random.choice(x)#choose a random variable for comparing

def first_var(a):#first variable is 0 in the list
  return a[0]
  
def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
  
    qsort_fixed_pivot = lambda a: qsort(a, fix_pivot)
    qsort_random_pivot = lambda a: qsort(a, random_pivot)
    #ssort_call = ssort(sizes)
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)#why was this commented out
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist),#since we wanna see timsort too
            #time_search(ssort_call, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 
                                    'timsort!', 'selection_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
