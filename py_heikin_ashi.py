import pandas as pd
import numpy as np
def heiken_ashi(data):
  res=pd.DataFrame()
  try: 
    res["Date"]=data.index
   except:
    res["Date"]=data.index
  O=[0]
  O.extend(list((data.Close+data.Open)/2)[:-1])
  res["Open"]=O
  C=list((data.Close+data.Open+data.High+data.Low)/4)
  res["High"]=np.array(data.High)
  res["Low"]=np.array(data.Low)
  res["Close"]=C
  return(res)
