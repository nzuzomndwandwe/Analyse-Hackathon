def bubble_sort(items):
    array = []
    for i in items:
        while len(items)>0:
            mini = min(items)
            array.append(mini)
            items.remove(mini)
    return array

def merge_sort(items):
    array = []
    for i in items:
        while len(items)>0:
            mini = min(items)
            array.append(mini)
            items.remove(mini)
    return array

def quick_sort(items):
    array = []
    for i in items:
        while len(items)>0:
            mini = min(items)
            array.append(mini)
            items.remove(mini)
    return array
    
