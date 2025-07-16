class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        for house in houses:
            pos = bisect.bisect_left(heaters, house)
            left_distance = float('inf') if pos == 0 else house - heaters[pos - 1]
            right_distance = float('inf') if pos == len(heaters) else heaters[pos] - house
            closest_heater_distance = min(left_distance, right_distance)
            max_radius = max(max_radius, closest_heater_distance)
        
        return max_radius