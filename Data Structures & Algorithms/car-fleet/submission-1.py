class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse= True)
        #stack = []
        fleets = 0
        slowest_time = 0

        for p,s in cars:
            time = (target-p)/s
            #stack.append(time)

            # if(len(stack) >= 2 and stack[-1] <= stack[-2]):
            #     stack.pop()
            if time > slowest_time:
                fleets += 1
                slowest_time = time
        
        return fleets

        