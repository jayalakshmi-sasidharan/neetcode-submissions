class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while(stack 
            and temperature > temperatures[stack[-1]]
            ):
                previous_index = stack.pop()
                answer[previous_index] = i - previous_index
            stack.append(i)
        
        return answer
    

        # n = len(temperatures)
        # answer = [0] * n

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             answer[i] = j - i
        #             break
        
        # return answer
