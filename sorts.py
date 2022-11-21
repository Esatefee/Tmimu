# Selection sort

def selection_sort(x):
    for i in range(len(x)-1):
        b = x[i]
        b1 = i
        for j in range(i+1, len(x)):
            if x[j] < b:
                b = x[j]
                b1 = j
        till = x[i]
        x[i] = x[b1]
        x[b1] = till
    print(x)
a = [3, 4, 1, 1000, 25, 35, 111]
selection_sort(a)

#Bubble sort

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i -1):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1],a[j]
    print(a)


a = [3, 4, 1, 1000, 25, 35, 111]

bubble_sort(a)

# Insertion sort

def insertion_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and value < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    print(a)
a = [3, 4, 1, 1000, 25, 35, 111]
insertion_sort(a)
