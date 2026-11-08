class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. 建一个空字典，用来记下“见过的数字”和“它的下标”
        num_dict = {}
        
        # 2. 遍历数组，同时拿下标 i 和数值 num
        for i, num in enumerate(nums):
            # 3. 计算需要找的另外一半
            c = target - num
            
            # 4. 去字典里查一下（而不是去列表里查，字典查得快且不会找自己）
            if c in num_dict:
                # 找到了！直接返回字典里 c 的下标，和当前的下标 i
                return [num_dict[c], i]
            
            # 5. 如果没找到，就把自己存进字典，留给后面的人配对
            num_dict[num] = i
            
        return []