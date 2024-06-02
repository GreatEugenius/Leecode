class MyHashSet2(object):

    def __init__(self):
        self.ans = [False] * (10 ** 6 + 1)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.ans[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.ans[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.ans[key]

class MyHashSet(object):

    def __init__(self):
        self.ans = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.ans[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.ans[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.ans.get(key,False)

test=MyHashSet()
test.add(1)
print(test.contains(1))
print((test.contains(2)))
# d={}
# d[1]=1
# print(d.get(2,0))