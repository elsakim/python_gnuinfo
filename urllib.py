import urllib.request as req

reObj = req.urlopen('http://class.gnu.ac.kr/~jslee/big/ex1.html')
print(reObj)

status = reObj.getheaders()
print(status)
