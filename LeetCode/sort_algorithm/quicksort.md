```
def quick_sort(nums):
    def q_sort(nums, low, high):
        if low < high:
            pivot = parition(nums, low, high)
            q_sort(nums, low, pivot - 1)
            q_sort(nums, pivot + 1, high)

    #用这个parition
    def parition(nums, low, high):
        pivot = nums[low]
        i, j = low, high
        while i < j:
            while (i < j and nums[j] >= pivot):
                j -= 1
            nums[i] = nums[j] #把小的数放到前面
            while (i < j and nums[i] <= pivot):
                i += 1
            nums[j] = nums[i] #把大的数放到后面 
        #退出While时,i=j
        nums[i] = pivot #把pivot这个值放到nums[i]
        return i 

    return q_sort(nums, 0, len(nums) - 1) 
    # 稳定性：不稳定
    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(n^2)

nums = [5, 9, 1, 11, 6, 7, 2, 4]

if __name__ == "__main__":
    quick_sort(nums)
    print(nums)
    # [1, 2, 4, 5, 6, 7, 9, 11]
```
