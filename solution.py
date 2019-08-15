import abc


class Solution:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def isInterleave(self, s1, s2, s3):
        pass


class Solution1(Solution):
    def __init__(self):
        self.found = dict()

    def isInterleave(self, s1, s2, s3):
        return self.isInterleaveFrom(s1, 0, s2, 0, s3)

    def isInterleaveFrom(self, s1, i1, s2, i2, s3):
        if (i1,i2) not in self.found:
            if i1 == len(s1) and i2 == len(s2):
                if i1 + i2 == len(s3):
                    result = True
                else:
                    result = False
            elif i1 < len(s1) and i2 < len(s2):
                if s1[i1] == s3[i1 + i2] and s2[i2] == s3[i1 + i2]:
                    result = self.isInterleaveFrom(s1, i1 + 1, s2, i2, s3) or self.isInterleaveFrom(s1, i1, s2, i2 + 1,
                                                                                                    s3)
                elif s1[i1] == s3[i1 + i2]:
                    result = self.isInterleaveFrom(s1, i1 + 1, s2, i2, s3)
                elif s2[i2] == s3[i1 + i2]:
                    result = self.isInterleaveFrom(s1, i1, s2, i2 + 1, s3)
                else:
                    result = False
            elif i1 < len(s1):
                result = s1[i1:] == s3[i1 + i2:]
            else:
                result = s2[i2:] == s3[i1 + i2:]
            self.found[(i1, i2)] = result
        return self.found[(i1, i2)]
