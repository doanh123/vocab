import urllib2, re

def readsitecontent(url):
    content = urllib2.urlopen(url).read(70000)
    return content

def findimage(content):
    links = []
    index1, index2, index3, index4  = (0,0,0,0)
    for i in range(2):
       index1 = content.find("http://ts1",index1) + 1
       links.append(content[index1-1:content.find("&",index1)])
        
       index2 = content.find("http://ts2",index2) + 1
       links.append(content[index2-1:content.find("&",index2)])

       index3 = content.find("http://ts3",index3) + 1
       links.append(content[index3-1:content.find("&",index3)])

       index4 = content.find("http://ts4",index4) + 1
       links.append(content[index4-1:content.find("&",index4)])
    return links


sitecontent = readsitecontent("http://bing.com/images/search?q=dog")
print findimage(sitecontent)
#print readsitecontent("http://bing.com/images/search?q=cats")
