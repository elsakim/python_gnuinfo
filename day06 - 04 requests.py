import requests as rq

rq.get("http://pythonscraping.com/pages/page.html")
rq.get("http://pythonscraping.com/pages/page1.html")

resObj = rq.get("http://pythonscraping.com/pages/page1.html")
print(resObj)

print(resObj.status_code)
headDict = resObj.headers
print(headDict)


for hear in headDict :
    print(hear, " => " , headDict[hear])


print(resObj.text)
print(resObj.content)
