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

def bingimageurl(url):
    return findimage(readsitecontent(url))

def bingimagesearch(word):
    url = "http://bing.com/images/search?q=" +word
    return findimage(readsitecontent(url))

#sitecontent = readsitecontent("http://bing.com/images/search?q=dog")
#print findimage(sitecontent)
#print readsitecontent("http://bing.com/images/search?q=cats")

""" get definition and sound files """
def getaudio(url):
    content = readsitecontent(url)
    links =[]
    audio = content.find("audio")
    start1= content.find("http",audio)
    end1 = content.find("mp3", audio)
    links.append(content[start1:end1 + 3])
    return links

def getdictionaryaudio(word):
    """takes any word and returns the audio file from dictionary.reference.com"""
    url = "http://dictionary.reference.com/browse/" + str(word)
    return getaudio(url)

def getaudiotest():
    """looks up the audio file for the word tree"""
    print getaudio("http://dictionary.reference.com/browse/tree")
