class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        end=intervals[0][1]
        count=len(intervals)-1
        for i in range(1,len(intervals)):
            if(intervals[i][0]>=end):
                end=intervals[i][1]
                count=count-1
        return count

test=Solution()


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(test.eraseOverlapIntervals(intervals))