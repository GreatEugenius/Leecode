class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ##方法1
        # flowerbed.insert(0, 0)
        # flowerbed.append(0)
        # for i in range(1,len(flowerbed)-1):
        #     if(flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
        #         flowerbed[i] = 1
        #         n = n - 1
        #         print(i)
        #     if (n <= 0):
        #         return True
        # return False

        # 方法2
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        i=1
        while(i<len(flowerbed)-1):
            if (flowerbed[i] == 0):
                if(flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n = n - 1
                    print(i)
                else:
                    i = i + 1
            if (n <= 0):
                return True
            i=i+2
        return False



test=Solution()

flowerbed = [1,0,0,0,1]
n = 2

print(test.canPlaceFlowers(flowerbed,n))