import urllib.request

client_id = "qOt_gqRZWOPjQZfL7dXP"
client_secret = "9yuHTz94mv"
search_text = urllib.parse.quote("빅데이터")
page_start = 1   
display = 5


# 'news', 'blog', 'cafearticle' 'movie' 'encyc'
url = "https://openapi.naver.com/v1/search/news?query=%s&start=%s&display=%s" %(search_text,page_start, display )# + search_text  # json 결과
#url = "https://openapi.naver.com/v1/search/encyc?query=%s&start=%s&display=%s" % (search_text,page_start, display )
#url = "https://openapi.naver.com/v1/search/news.xml?query=" + search_text # xml 결과

reqObj = urllib.request.Request(url)
print(reqObj)

reqObj.add_header("X-Naver-Client-Id",client_id)
reqObj.add_header("X-Naver-Client-Secret",client_secret)

htmlObj = urllib.request.urlopen(reqObj)
print(htmlObj)

htmlObj_body = htmlObj.read()
print(htmlObj_body.decode('utf-8'))
