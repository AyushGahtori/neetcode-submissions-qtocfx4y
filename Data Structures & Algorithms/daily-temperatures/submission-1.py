class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for i, t in enumerate(temps):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i -  index
            stack.append((i, t))
        return res        


        