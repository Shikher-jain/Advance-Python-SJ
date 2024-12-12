import pandas
data={
    "Studests":["abcd","efgh","ijkl","mnop"],
    "sports":["hockey","cricket","football","baseball"],
    "marks":[98,86,85,90]
    }

print(data)
print(dir(pandas))
df=pandas.DataFrame(data,index = ["type 1","type 2","type 3","type 4"])
print(df)
# display(df)
print(df.index)