def move_zeros(a_list):
    """
    this function is given a list. In the original list, zeros is moved to the last.

    idea: move all the non-zero values to the left

    O(1)

    cons: many swaps => have to keep the relative position

    """
    # left = 0
    # right = 0
    # while right<len(a_list):
    #     if a_list[right]!=0:
    #         temp = a_list[right]
    #         a_list[right] = a_list[left]
    #         a_list[left] = temp
    #         left+=1
    #     right+=1

    # improvements: do not swap 0 to the right. Instead, write all the zeros to the end. (fewer writes)

    left = 0
    right = 0
    while right < len(a_list):
        if a_list[right]!=0:
            a_list[left] = a_list[right]
            left+=1
        right+=1
    while left<right:
        a_list[left]=0
        left+=1

    
    

if __name__ == "__main__":
    case1=[1,0,2,3,4,0,5]
    case2 = [0,0,1,2,0,3]
    move_zeros(case1)
    move_zeros(case2)
    assert case1 == [1,2,3,4,5,0,0]
    assert case2 == [1,2,3,0,0,0]



