class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        '''
        # brute force
        ans = len(nums)+1
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= s:
                    if j-i+1 < ans:
                        ans = j-i+1
                    break
        if ans == len(nums)+1:
            return 0
        return ans
        '''
        # optimized
        if len(nums) == 0:
            return 0
        fl = 0
        finalStartPointer = -1
        finalEndPointer = len(nums)
        currentStartPointer = 0
        currentEndPointer = 0
        currentSum = nums[0]
        while(True):
            while currentSum < s:
                currentEndPointer += 1
                if currentEndPointer > len(nums)-1:
                    fl=1
                    break
                currentSum += nums[currentEndPointer]
            if fl==1:
                break
            if finalEndPointer-finalStartPointer > currentEndPointer-currentStartPointer:
                finalStartPointer = currentStartPointer
                finalEndPointer = currentEndPointer
            while currentSum >= s:
                currentSum -= nums[currentStartPointer]
                currentStartPointer += 1
            if finalEndPointer-finalStartPointer > currentEndPointer-currentStartPointer+1:
                finalStartPointer = currentStartPointer-1
                finalEndPointer = currentEndPointer    
        if finalStartPointer == -1:
            return 0
        return finalEndPointer-finalStartPointer+1;
