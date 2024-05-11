# 반복문으로 이진탐색 구현하기
def binary_search(nums, key):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        if nums[mid] == key:
            return mid
        elif key < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 재귀로 이진탐색 구현하기
def binary_search_recursion(nums, key, start, end):
    while start < end:
        mid = (start + end) // 2
        if nums[mid] == key:
            return mid
        elif key < nums[mid]:
            binary_search_recursion(nums, key, start, mid - 1)
        else:
            binary_search_recursion(nums, key, mid + 1, end)
    return None

