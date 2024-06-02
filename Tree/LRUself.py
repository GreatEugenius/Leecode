class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value=value
        self.prev=None
        self.post=None
class DoubleLink(object):
    def __init__(self):
        self.length=0
        self.head=None
        self.tail=None


