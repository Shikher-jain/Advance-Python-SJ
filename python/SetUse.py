# class Solution:
#     def checkSubset(self, A, B):
#         is_subset = True
#         for elem in A:
#             if elem not in B:
#                 is_subset = False
#                 break
    
#         if is_subset:
#             return True
#         else:
#             return False

        
# if __name__ == "__main__": 

#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     a=set(a);b=set(b);
#     ob = Solution()
#     res = ob.checkSubset(a,b)
#     print(res)

a={4,5,6}
b={2,8,6}
print(a-b)
print(type(a))