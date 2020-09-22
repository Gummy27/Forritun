def bubbleSortWeb(listi): 
    listi = listi[:]
    n = len(listi) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if listi[j] > listi[j+1] : 
                listi[j], listi[j+1] = listi[j+1], listi[j] 

    return listi