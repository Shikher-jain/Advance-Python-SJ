import cv2 
import numpy
import pandas as pd
# import pandas
# from pandas import DataFrame
# from pandas import DataFrame
import sys
print(sys.executable)
print("Version of cv2:",cv2.__version__)
print("Version of numpy:",numpy.__version__)
data={
    "Studests":["abcd","efgh","ijkl","mnop"],
    "sports":["hockey","cricket","football","baseball"],
    "marks":[98,86,85,90]
    }
print(data)
# df=pandas.DataFrame(data,index = ["type 1","type 2","type 3","type 4"])
df=pd.DataFrame(data,index = ["type 1","type 2","type 3","type 4"])
print(df)
print(dir(pd))
# print(dir(pandas))
df=pd.DataFrame(data)
# df=pandas.DataFrame(data)
print(df)
# display(df)
print(df.index)
print(df)