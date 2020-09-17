class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=i
            else:
                dic.pop(i)
        for i in nums:
            if i in dic:
                return dic[i]
            
            
        