class LAMBDA_FX:
    def ArrayMultiply(arr,n):
        res=lambda a:arr * n
        return res
    
ans=LAMBDA_FX.ArrayMultiply([1,2,3,4,5],2)
print(ans)
