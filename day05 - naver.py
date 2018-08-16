import urllib.request
import  json
import  os

client_id = "qOt_gqRZWOPjQZfL7dXP"
client_secret = "9yuHTz94mv"
search_text = urllib.parse.quote("빅데이터")
page_start = 1   
display = 5

url = "https://openapi.naver.com/v1/search/news?query=%s&start=%s&display=%s" %(search_text, page_start, display )

reqObj = urllib.request.Request(url)
print(reqObj)


reqObj.add_header("X-Naver-Client-Id", client_id)
reqObj.add_header("X-Naver-Client-Secret", client_secret)

htmlObj = urllib.request.urlopen(reqObj)
print(htmlObj)


htmlObj_body = htmlObj.read()
html_Obj = htmlObj_body.decode('utf-8')  #결과는 문자열


with open(os.path.join('naver_result.json'), 'w+') as json_file:
    json.dump(html_Obj, json_file)


