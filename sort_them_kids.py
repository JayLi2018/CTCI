# A collection of sorting algorithms implementations

# Group A: in-place sorting

# 1: Selection Sort:
    # Use 2 arrays, 1st is sorted, 2nd is unsorted
    # In each iteration, we find a minimum value from
    # unsorted array, and place it to the end of sorted
    # array
    # Time Complexity: O(n^2): nested loops
    # Space Complexity: O(1)

def selection_sort(ulist, ascend=True):

    l = len(ulist)
    if(l<=1):
        return ulist
    sorted_ind = 0
    while(sorted_ind<l):
        add_ind, add_num = sorted_ind, ulist[sorted_ind]
        for i in range(sorted_ind+1, l):
            if(ascend):
                if(ulist[i]<add_num):
                    add_ind, add_num = i, ulist[i]
            else:
                if(ulist[i]>add_num):
                    add_ind, add_num = i, ulist[i]

        ulist[sorted_ind], ulist[add_ind] = ulist[add_ind],ulist[sorted_ind]
        sorted_ind+=1

    return ulist

# 2: Bubble Sort:
    # Each pass, swap 2 adjacent numbers 
    # when the relative order between the 
    # two is wrong, can stop early without 
    # going through all n pass

    # Time Complexity: O(n^2) because worst case we need to 
    # go through all n pass and do n bounded comparisions 
    # within each pass
    # Space Complexity: O(1), no extra space needed

def bubble_sort(ulist, ascend=True):

    l = len(ulist)
    if(l<=1):
        return ulist
    n=0
    while(n<l-1):
        no_swap = True # a flag to see if we can stop early
        i,j = 0,1
        while(j<=l-1-n):
            if(ascend):
                if(ulist[j]<ulist[i]):
                    if(no_swap):
                        no_swap=False
                    ulist[i], ulist[j] = ulist[j], ulist[i]
            else:
                if(ulist[j]>ulist[i]):
                    if(no_swap):
                        no_swap=False
                    ulist[i], ulist[j] = ulist[j], ulist[i]
            i+=1
            j+=1
        if(no_swap):
            break
        n+=1

    return ulist



if __name__ == '__main__':
    x = selection_sort([1,1,2,3], ascend=False)
    print(x)

    x = bubble_sort([1,7,10,3], ascend=False)
    print(x)