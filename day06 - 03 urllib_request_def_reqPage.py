from  urllib.request  import  urlopen
from urllib.error import HTTPError

#웹 페이지 요청하는 함수
def reqPage(url) :    
    try :
        htmlObj = urlopen(url)
  
    except HTTPError as e :
        print(e)
        return None

    else:
        return htmlObj



pageObj = reqPage("http://pythonscraping.com/pages/page1.html")

if pageObj == None :
    print("페이지를 찾지 못했습니다.")
else:
    print(pageObj.read())
    

