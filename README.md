# google_word_crawling
구글 단어 검색 크롤링

spec:
`python 3.x`
`pandas`
`fastAPI`
`uvicorn`
`docker`

url: 
`localhost:[port]/docs` 


## Requirements

```
  $ pip install fastapi
```

```
  $ pip install uvicorn[standard]
```

Docker</br>
**window 설치 참고**</br>
https://docs.docker.com/desktop/install/windows-install/</br>

## Usage
uvicorn으로 사용
```
  uvicorn main:app
```

### docker
#### docker hub
```
  docker pull jjam89/fastapi:v1
```

#### local
이미지
```
  docker build -t fastApi:v1 .
```

실행
```
  docker run --rm -p [port]:[port] fastapi:v1
```




### References
https://fastapi.tiangolo.com/</br>
https://www.uvicorn.org/</br>
https://www.promptcloud.com/blog/data-scraping-vs-data-crawling/</br>
