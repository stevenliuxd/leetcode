def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort() 
        
        # Initialize Pointers
        i = 0
        j = 1
        n = len(nums) - 1
        m = len(nums) - 2
        
        # Answer list
        output = []
        
        while (m-j) >= 1:
            
            tot = nums[i] + nums[j] + nums[n] + nums[m]
            print("m:" + str(m) + "  |  " + "j:" + str(j) + "  Total sum:" + str(tot) + "  pointing to: " + str(nums[i])+ str(nums[j])+ str(nums[m])+ str(nums[n]))

            if tot < target:
                i+=1
                j+=1
            elif tot > target:
                m-=1
                n-=1
            elif tot == target:
                ans = [nums[i], nums[j], nums[n], nums[m]]
                output.append(ans)
                i+=1
                j+=1
        
        return output

print(fourSum([1,0,-1,0,-2,2], 0))