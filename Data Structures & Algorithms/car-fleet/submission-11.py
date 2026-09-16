class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # O(nlog(n))
        cars = sorted(zip(position,speed))
        max_time = 0
        fleet = 0
        while cars:
            p, s = cars.pop()
            time = (target - p) / s
            if time > max_time:
                max_time = time
                fleet += 1
        return fleet