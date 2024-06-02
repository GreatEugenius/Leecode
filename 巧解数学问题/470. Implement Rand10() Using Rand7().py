# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        rand =39
        while rand <40:
            rand = (rand7()-1)*7+rand7()
        return rand%10 +1