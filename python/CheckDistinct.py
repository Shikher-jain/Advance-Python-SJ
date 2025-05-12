class Solution:
    def checkDistinct(self, A):

        if len(A) != len(set(A)):
            return "Not Distinct"
        else:
            return "Distinct"

if __name__ == "__main__": 
    a=tuple(map(int,input().split()))
    ob = Solution()
    res = ob.checkDistinct(a)
    print(res)
