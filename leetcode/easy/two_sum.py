def twoSum():
    nums = [8, 7, 11, 15]
    target = 15
    for num in nums:
        comparison = nums[0] + nums[1]
        if comparison == target:
            return print(comparison)
        else:
            comparison





def tweeSum():
    nums = [8, 7, 11, 15]
    target = 15
    for index1, num in enumerate(nums):
        for index2 in range(index1 + 1, len(nums)):
            comparison = num + nums[index2]
            if comparison == target:
                return print(comparison)

tweeSum()


def driesum():
    hashmap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i
        return