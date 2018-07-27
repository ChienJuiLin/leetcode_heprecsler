
class Solution:

    nc = [ ['a','b','c'],
           ['d','e','f'],
           ['g','h','i'],
           ['j','k','l'],
           ['m','n','o'],
           ['p','q','r','s'],
           ['t','u','v'],
           ['w','x','y','z'] ]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        ansf = list()
        curCs = ''
        self.nt(ansf,curCs,digits)
        return ansf


    def nt(self,ans,curC,d):
        if len(d) == 1:
            for x in self.nc[int(d[0])-2]:
                curc = curC
                curc = curc + x
                ans.append(curc)

        else:
            for x in self.nc[int(d[0])-2]:
                curC = curC + x
                self.nt(ans,curC,d[1:])
                curC = curC[:len(curC)-1]
