class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candys = [1 for _ in range(len(ratings))]

        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                candys[i]=candys[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1] and candys[i]<=candys[i+1]):
                candys[i]=candys[i+1]+1
        sum=0
        for i in range(len(candys)):
            sum=sum+candys[i]
        return sum


test=Solution()


ratings=[1,2,87,87,87,2,1]
print(test.candy(ratings))