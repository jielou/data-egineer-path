def binary_search(sorted_list, value):
    # suppose sorted_list is sorted in advance
    # return the index, if not return None
    lower = 0
    higher = len(sorted_list)-1

    while lower<=higher:
        mid = (lower+higher)//2 # get the index of mid point
        num_mid = sorted_list[mid]
        if num_mid==value: # find
            return mid
        elif num_mid<value: # in the left half
            lower=mid+1
        else: # in the right half
            higher = mid-1

if __name__ == "__main__":
    assert binary_search([1,2,3,4,5,6],0) is None
    assert binary_search([1,2,3,4,5,6],1) ==0
    assert binary_search([1,2,3,4,5,6],2) ==1
    assert binary_search([1,2,3,4,5,6],3) ==2
    assert binary_search([1,2,3,4,5,6],6) ==5
    assert binary_search([1,2,3,4,5,6],7) is None
    
