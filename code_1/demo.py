# -*- coding: utf-8 -*-
'''
 demo.py
 @author： wyf
 @created： 2021-08-26T16:52:17.777Z+08:00
 @last-modified： 2021-08-26T18:01:43.395Z+08:00
 @description： 
'''
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsLen = len(nums)
        for i in range(numsLen):
            if i+1 == numsLen:
                break
            else:
                for x in range(i+1, numsLen): 
                    temp = []      
                    if nums[i] + nums[x] == target:
                        temp.append(i)
                        temp.append(x)
                        return temp
            
if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2,7,11,15], 9)
    for i in r:
        print(i)
