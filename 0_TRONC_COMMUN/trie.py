import random
# trie par selection

def selection_sort(l):
    for i in range(0, len(l)-1):
        min = l[i]
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < min:
                min = l[j]
                min_index = j
        l[min_index] = l[i]   
        l[i] = min            
    return l

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

l = generate_random_list(20, -100, 100)
print("UNSORTED:", l)


print("sorted",selection_sort(l))

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = [x for x in lst[1:] if x <= pivot]
        right = [x for x in lst[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst
