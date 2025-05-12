class Solution:
    def Query(self, dict, query):
        for i in query:
            if i in dict:
                print(dict[i])
            else:
                print(None)

if __name__ == "__main__": 
    a = list(map(int,input().split()))
    b = list(map(str,input().split()))
    query = list(map(int,input().split()))
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = b[i]
    ob = Solution()
    res = ob.Query(dict,query)
