class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        end=points[0][1]
        count=1
        for i in range(1,len(points)):
            if(points[i][0]>end):
                end=points[i][1]
                count=count+1
        return count

test=Solution()


points = [[1,2],[2,3],[3,4],[4,5]]

print(test.findMinArrowShots(points))