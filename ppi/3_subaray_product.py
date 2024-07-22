def check_sublist_product(nums, target):
    n = len(nums)
    left = 0
    product = 1

    for right in range(n):
        product *= nums[right]

        while product >= target and left <= right:
            if product == target:
                return True
            
            product //= nums[left]
            left += 1
    
    return False

print(check_sublist_product([1,2,3,4], 6))
print(check_sublist_product([1,2,8,3,4], 6))
print(check_sublist_product([1,2,3,4], 15))
print(check_sublist_product([7,2,3,4], 7))
print(check_sublist_product([1,2,3,4], 8))
