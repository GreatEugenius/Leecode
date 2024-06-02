class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:(-x[0],x[1]))
        res=[]
        for i in people:
            res.insert(i[1],i)
        return res
    

test=Solution()


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(test.reconstructQueue(people))