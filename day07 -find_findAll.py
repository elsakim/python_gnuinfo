from bs4 import BeautifulSoup
'''
#text 매개변수 
htmlObj = """ <font color="blue">best</font>
<font color="blue">best of best</font>
<font color="blue">best</font>best<br/> """

bsObj = BeautifulSoup(htmlObj, "lxml")
wordList = bsObj.findAll(text = "best")
print('text 매개변수  = ', len(wordList))


'''
htmlObj = """<p>I am a girl</p>
             <p>best of best</p>
             <font color="blue">best</font>best<br/>"""
bsObj = BeautifulSoup(htmlObj, "lxml")

findList = bsObj.findAll(text = "best")
print('\n', findList)
print('text 매개변수 = ',len(findList), '개') #2개


# limit 매개변수 - 찾고 싶은 갯수 지정
htmlObj = """<p>I am a girl</p>
                <font color="blue">best</font>
                <font color="blue">best</font>best<br/>"""

bsObj = BeautifulSoup(htmlObj, "lxml")
findList = bsObj.findAll(text = "best", limit = 2)
print('\n', findList)
print('limit 매개변수 = ', len(findList), '개')



#keyword 매개변수
htmlObj = """<font color="blue">jslee</font>
             <font color="blue">ekkim</font>
             <font color="red">shpark</font>"""

bsObj = BeautifulSoup(htmlObj, "lxml")

findList = bsObj.findAll(color = "blue")
print(findList)

findList = bsObj.findAll("", {"color":"blue"})
print('\n', findList)






























