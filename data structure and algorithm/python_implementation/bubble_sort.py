def bubble_sort(any_list, ascending=True):
    # O(n*n)
    for _ in any_list:
        for i in range(0,len(any_list)-1):
            first,second = any_list[i],any_list[i+1]
            if ascending:
                if first>second:
                    any_list[i], any_list[i+1]=second, first
            else:
                if first<second:
                    any_list[i], any_list[i+1]=second, first

def bubble_sort_advanced(any_list, ascending=True):
    # optimized: everytime the biggest/smallest one will be pop to the end.
    for j in range(len(any_list)-1,0,-1):
        for i in range(0,j):
            first,second = any_list[i],any_list[i+1]
            if ascending:
                if first>second:
                    any_list[i], any_list[i+1]=second, first
            else:
                if first<second:
                    any_list[i], any_list[i+1]=second, first

def is_sorted(any_list, ascending=True):
    for i in range(0, len(any_list)-1):
        first,second = any_list[i],any_list[i+1]
        if ascending:
            if first>second:
                return False
        else:
            if first<second:
                return False
    return True

if __name__ == "__main__":
    example = [10,6,8,3,2,7]
    bubble_sort_advanced(example)
    print(example)
    print(is_sorted(example))
    bubble_sort_advanced(example, ascending=False)
    print(example)
    print(is_sorted(example,ascending=False))
    
    
