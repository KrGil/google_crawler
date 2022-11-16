from fastapi import APIRouter, HTTPException
import os
import pandas as pd

router = APIRouter(
    prefix="/sort"
)

@router.get('/{fileName}')
def saveOrderByDate(originFileName: str, tobeFileName: str): 
    originFileName = originFileName.rstrip(".csv")
    
    try:
        df = pd.read_csv('./'+originFileName+'.csv')
        df.sort_values(by='날짜', ascending=False, inplace=True, ignore_index=True)
        df.to_csv('./'+tobeFileName+'_sorted.csv')
        return df

    except Exception:
        msg = {"ERROR":"File Not Found Error", "EXIST":[]}
        msg["EXIST"].append(showfiles())
        raise HTTPException(status_code=404, detail=msg)

def showfiles():    
    dir_path = os.getcwd()
    fileList = []

    for file in os.listdir(dir_path):
        if '.csv' in file:
            fileList.append(file)
    
    return fileList