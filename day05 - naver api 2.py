import urllib.request

client_id = "qOt_gqRZWOPjQZfL7dXP"
client_secret = "9yuHTz94mv"
search_text = urllib.parse.quote("빅데이터")
page_start = '1'
display = '5'


    # 'news', 'blog', 'cafearticle' 'movie' 'encyc'
#url = "https://openapi.naver.com/v1/search/news?query=" + search_text  # json 결과
url = "https://openapi.naver.com/v1/search/news?"
#url = "https://openapi.naver.com/v1/search/news.xml?query=" + search_text # xml 결과

reqObj = urllib.request.Request(url)
datainfo = "query=" & search_text & "&start=" & page_start & "&display=" & display
#data = "query=빅데이터&page_start=1&display=5"
reqObj = urllib.request.Request(url,data=datainfo, headers={"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret})



htmlObj = urllib.request.urlopen(reqObj)
print(htmlObj)


rescode = htmlObj.getcode()    
if(rescode==200):
    htmlObj_body = htmlObj.read()
    print(htmlObj_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


   
