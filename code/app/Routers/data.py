from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup as bs
from pydantic import BaseModel
import csv
import requests
import pandas as pd
import datetime
import os
router = APIRouter(
    prefix="/search/v1"
)

class RequestParam(BaseModel):
    word: str
    limitPage: int


@router.post('/')
def save(request: RequestParam):
    search = request.word
    limit = request.limitPage

    validate(limit)

    fileNameList = ["./"+search+".csv"]
    fileNameList.append("./logs/"+search+"_"+datetime.datetime.now().strftime('%Y-%m-%d')+".csv")
    os.makedirs("./logs/", exist_ok=True)
    articleLists = []
    
    for n in range(limit):
        params = {"q": search, "hl": "ko", "start": n*10}

        header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
        cookie = {"CONSENT": "YES"}
        url = "https://www.google.com/search?"

        res = requests.get(url, params=params, headers=header, cookies=cookie)
        soup = bs(res.text, "html.parser")
        
        articleLists.append(soup.find_all("div", "kvH3mc BToiNc UK95Uc")) 
        
    return pd.DataFrame(saveFile(fileNameList, articleLists))

def saveFile(fileNameList, articleLists):
    for fileName in fileNameList:
        f = open(fileName, "w", encoding="utf-8-sig", newline='')
        writer = csv.writer(f)
        
        writer.writerow(['제목', '날짜', '내용'])
        result = {"제목":[],"날짜":[],"내용":[]}
        for articleList in articleLists:
            for i, article in enumerate(articleList):
                h3 = article.find("h3", attrs={"class": "LC20lb MBeuO DKV0Md"}).get_text()
                
                date = article.find("span", {"class": "MUxGbd wuQ4Ob WZ8Tjf"})
                if date is None:
                    date = "0000.00.00"
                else:
                    date = date.get_text().replace('—', '').replace(' ', '').strip()
                    if date.endswith('\.'):
                        date[:-1]

                content = article.find("div", {"class": "Z26q7c UK95Uc"}).get_text().replace(date, '').replace('\xa0', '')
                data = [h3, date, content]
                
                result["제목"].append(h3)
                result["날짜"].append(date)
                result["내용"].append(content)

                writer.writerow(data)
    return result

def validate(limit: int):
    if 10 < limit or limit < 1:
        raise HTTPException(
            status_code=400, 
            detail={"ERROR":"Invalid argument", "HINT":"최소 1 페이지에서 최대 10 페이지까지 검색할 수 있습니다."}
        )