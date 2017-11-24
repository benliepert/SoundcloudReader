

import urllib.request as web
import webbrowser

def reader(url):
    '''
    Author: Ben Liepert, 10/22/15
    Purpose (so far): To create a list with the names of all the songs in a
      playlist located at the given parameter url and count the number of songs
    Parameters:
      url = a soundcloud playlist url
    '''
    List_O_Songs = []

    ## 'https://soundcloud.com/benliepert/sets/all-time-best-2-0-1'

    webpage = web.urlopen(url)
    print(webpage.read())
##    line = webpage.readline()
##    line = line.decode('utf-8')
##    counter = 0
##    
##    while '</header>' not in line:
##        
##        line = webpage.readline()
##        line = line.decode('utf-8')
##
##    while '</section>' not in line:
##        
##        line = webpage.readline()
##        line = line.decode('utf-8')
##        
##        if '<h2 itemprop="name">' in line:
##            
##            x = line[::-1]
##            y = line.find('</a>')
##            use = x.find('>"')
##            L = line[-use:y]
####            if '&amp;' in line:
####                L.replace('&amp;', '&')
##                
##            List_O_Songs.append(L)
##            ##print(L)
##            counter+=1
##            ##print('Song Number = ' + str(counter))
##            ##print()
        
    
    webpage.close()

    return List_O_Songs

print(reader("https://soundcloud.com/benliepert/sets/cruise-tunes"))

def listFixer(url):
    '''
    Author: Ben Liepert, 10/23/15
    Purpose: to take the list produced by the 'reader' and fix it so the proper
      &, ", ' symbols appear instead of their html symbolic euqivilants
    Parameters:
      url = a url of a soundcloud playlist

    '''
    L = reader(url)
    newL = []

    for item in L:
        
        if '&amp;' in item:
            item = item.replace('&amp;', '&')
        if '&quot;' in item:
            item = item.replace('&quot;', '"')
        if '&#x27;' in item:
            item = item.replace('&#x27;', "'")

        newL.append(item)

    return newL


def youtubeLinkMaker(url):

    List = listFixer(url)
    fixedList = []

    for item in List:
        
        if ' & ' in item:
            item = item.replace(' & ','%26')
        item = item.replace(' ','+')
        if "'" in item:
            item = item.replace("'",'%27')
        if '(' in item:
            item = item.replace('(', '%28')
        if ')' in item:
            item = item.replace(')', '%29')
        if '[' in item:
            item = item.replace('[', '%5B')
        if ']' in item:
            item = item.replace(']', '%5D')
        if ',' in item:
            item = item.replace(',','%2C')
        if '+~+' in item:
            item = item.replace('+~+','+')
        
            
        fixedList.append(item)

    linkList = []
    
    for item in fixedList:
        item = "'http://www.youtube.com/results?search_query=" + item + "'"
        linkList.append(item)

        
    return linkList


def youtubeSearchOpener(url):
    '''
    Purpose: Opens a youtube search for the song title of every song in the
      playlist found at the given soundcloud url

    '''

    LinkList = youtubeLinkMaker(url)

    for i in range(3):
        
        
            searchURL = LinkList[i]

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            webbrowser.get(chrome_path).open(searchURL)
            
            

def firstVideoFinder(url):

    searchLinkList = youtubeLinkMaker(url)

    for i in range(3):

        URL = searchLinkList[i]
        URL =  URL.encode('ascii','ignore')
        URL = URL.decode('utf-8')
        
        webpage = web.urlopen(URL)
        
        line = webpage.readline()
##        line = unicodeData.encode('ascii','ignore')
        
        line = line.decode('utf-8')
        
        counter = 0

        for line in webpage:
            
            while counter < 2096:
                
                line = webpage.readline()
                
                line = line.decode('utf-8')
                counter +=1
                
            while counter < 2099:
                line = webpage.readline()
                
                line = line.decode('utf-8')
                print(line)
                counter +=1

##x = youtubeLinkMaker('https://soundcloud.com/benliepert/sets/all-time-best-2-0-1')
##print(x[0])
##y = x[0]
##
##y = y.encode('ascii','ignore')
##y = y.decode('utf-8')
##webpage = web.urlopen(y)
    
        


def downloadLinkMaker(url):

    LinkList = [4,5,6] ## the function that gets actual video links

    ## Youtube Link: https://www.youtube.com/watch?v=IUGzY-ihqWc
    ## Download Link: http://www.flvto.biz/progress/mp3/yt_IUGzY-ihqWc/
    
    downloadLinkList = []
    
    for i in range(len(LinkList)):
        
        URL = LinkList[i]
        partURL = URL[32:]
        newURL = 'http://www.flvto.biz/progress/mp3/yt_' + partURL

        downloadLinkList.append(newURL)

    return downloadLinkList
        
        

            

##webOpener('https://soundcloud.com/benliepert/sets/all-time-best-2-0-1')
##('https://soundcloud.com/ataahking/sets/like-it-is-in-the-movies'))

  

##print(youtubeLinkMaker('https://soundcloud.com/benliepert/sets/all-time-best-2-0-1'))

## IDEAS

## get code for a given youtube search - find where the search request appears
##   in the url, replace with each song name

## find listen to youtube url when a youtube url is put in
## see if python can download automatically (the hard part)
## or if it can open it in the browser and the user must click

## https://www.youtube.com/results?search_query=search+dsafdsfad+dsafajdsfjkd
## youtube search spaces are replaced by + signs - use a built in
## & sign is '%26' in url
## ' is '%27' in url

##http://www.flvto.biz/progress/mp3/yt_DQ36ZiGnALU/
##https://www.youtube.com/watch?v=DQ36ZiGnALU

## read in the youtube page - make a counter for each line read
## while counter < some number (where the results start to appear) 2096
## just read over everything
## click the first (legitimate) result - make sure ads are accounted for









    
