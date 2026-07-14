class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(s)
        tArr = list(t)
        sArr.sort()
        tArr.sort()
        if(len(sArr) != len(tArr)):
            return False
        for x in range(0 ,len(sArr)):
            if( sArr[x] != tArr[x]):
                return False
        return True