# Time complexity -> O(N log(k))
# Space complexity -> O(k)

class Solution:
    def find_distance(self, point):
        x , y = point
        distance = ( x ** 2 + y **2 ) ** ( 0.5)
        return distance 

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        for point in points:
            distance = self.find_distance(point)
            heapq.heappush(closest_points, (distance,point))
            if len(closest_points) > k:
                heapq.heappop(closest_points)
        result = []
        for point in closest_points:
            result.append(point[1])
        return result
        
