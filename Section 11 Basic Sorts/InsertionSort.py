# BigO
# Worse O(n^2)
# Best for almost sorted data: O(n)
# Space: O(1)
# All three of these sort the list in place.
# That means that they do not create additional copies of the list.
# That means it the space complexity is O(1)


my_list = [1, 2, 4, 3, 5, 6]

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j-=1
    return my_list
        
print(insertion_sort([4,2,6,5,1,3]))
        