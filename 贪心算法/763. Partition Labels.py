class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        s=s+"*"
        alist=[]
        for i in s:
            if(i not in alist):
                alist.append(i)
        patition=[]
        for i in range(len(alist)):
            patition.append([s.find(alist[i]),s.rfind(alist[i])])
        begin=patition[0][0]
        end=patition[0][1]
        res=[]
        for i in range(1,len(patition)):
            if(patition[i][0]<end):
                if(patition[i][1]>end):
                    end=patition[i][1]
            if(patition[i][0]>end):
                res.append(end-begin+1)
                begin=patition[i][0]
                end=patition[i][1]

        return res

test=Solution()


s = "eccbbbbdec"

print(test.partitionLabels(s))