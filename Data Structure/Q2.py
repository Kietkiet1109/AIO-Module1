def exercise2(nums1, nums2):
    num_list = list()

    for num1 in nums1:
        if num1 in nums2:
            num_list.append(num1)

    return num_list


print(exercise2([1,2,2,1], [2,2]))
print(exercise2([4,9,5], [9,4,9,8,4]))
