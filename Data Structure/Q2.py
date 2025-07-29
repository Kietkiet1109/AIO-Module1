def intersection(lst1, lst2):
    num_list = list()

    for num1 in lst1:
        if num1 in lst2:
            num_list.append(num1)

    return num_list


test_list1 = [4, 9]
test_list2 = [9, 2]
print(intersection(lst1 = test_list1, lst2 = test_list2))

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(lst1 = nums1, lst2 = nums2))

num_list1 = [4, 9, 5]
num_list2 = [9, 4, 9, 8, 4]
print(intersection(lst1 = num_list1, lst2 = num_list2))
