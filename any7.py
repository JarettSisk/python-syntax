def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    # Loop through each num in list, if a match is found, return true
    for num in nums:
        if num == 7:
            return True
    # Else return false
    return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

