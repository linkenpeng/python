# coding:utf-8
# Practice of scraping web data with xpath
# by redice 2010.11.05

import codecs
import sys  
import urllib2
from urllib2 import URLError, HTTPError
import zlib
import sqlite3


try:
    import cPickle as pickle
except ImportError:
    import pickle
    

conn = sqlite3.connect("html_cache.db")
conn.text_factory = lambda x: unicode(x, 'utf-8', 'replace')
curs = conn.cursor()

#if htmls tables not exist,create it
#curs.execute('''CREATE TABLE if not exists htmls(url VARCHAR(255) UNIQUE,content BLOG,size INTEGER);''')
curs.execute('''CREATE TABLE if not exists htmls(url VARCHAR(255) UNIQUE,content TEXT,size INTEGER);''')
conn.commit()

def serialize(value):
    """convert object to a compressed pickled string to save in the db
    """
    #return sqlite3.Binary(zlib.compress(pickle.dumps(value, protocol=pickle.HIGHEST_PROTOCOL), 5))
    #return sqlite3.Binary(value)
    return value
    
def deserialize(value):
    """convert compressed pickled string from database back into an object
    """
    #return pickle.loads(zlib.decompress(value)) if value else value
    return value

# Fetch the target html
def gethtml(url):
    '''Fetch the target html'''
    try:
        # look up the html_cache.db first

        curs.execute("select * from htmls where url=?;" ,(url,))
        row = curs.fetchone()
        if row:
            # find the target
            #print deserialize(str(row[1]))
            return deserialize(str(row[1]))

        response = urllib2.urlopen(url)
        result = response.read()
        # insert into the html_cache.db
        curs.execute("insert into htmls values(?,?,?);", (url,serialize(result),len(result)))
        conn.commit()
        
        print "saved %s into html_cache.db" % (url)
        
        return  result
    except URLError, e:
        if hasattr(e, 'reason'):
            print 'Failed to reach a server.'
            print 'Reason: ', e.reason
            return 'None'
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            return 'None'
    #except:
        #return 'None'
    
# end def gethtml


import re

#Fetch the all string matched. Return a list.
def regexmatch(rule,str):
    '''Fetch the all string matched. Return a list.'''
    p = re.compile(rule)
    return p.findall(str)
#end def regexmatch


# decodeHtmlEntity
def decodeHtmlEntity(s) :
    '''decodeHtmlEntity'''
    if s=='' or not s:
       return ''
    result = s
    
    import locale
    result = result.decode(locale.getdefaultlocale()[1],"ignore").encode(locale.getdefaultlocale()[1]).replace("\xc2\xa0"," ")
    
    return result
# end def decodeHtmlEntity

#final result
dining_db = []

total = 0;

#debug
debug = 0

# Fetch menupalace.com's html
print 'Fetching html from http://menupalace.com ...'
html = gethtml('http://menupalace.com')

try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")




if html=='' or  html=='None':
    print "Can't get them html from http://menupalace.com"
    sys.exit()

try:
    tree = etree.HTML(html)
    nodes = tree.xpath("//table[@class='n_table']")
except:
    f = open("log.txt","wa")
    f.write(html)
    print("error to resolve the html http://menupalace.com")
    sys.exit()

for node in nodes:
    if debug and total>=10:
        break;

    n = node.xpath("./tr[1]/td[1]/img")
    # Fetch country
    country = ""
    if len(n)>0:
        country = decodeHtmlEntity(n[0].tail)
        country = country.strip()

    # Fetch all link    
    ls = node.xpath(".//a")

    # Through all link
    for l in ls:
        if debug and total>=10:
            break;
        
        #city
        city = decodeHtmlEntity(l.text)
        city = city.strip()
        
        prelink = l.get("href")
        link = prelink + "restaurants/restaurants.aspx"

        #print 'Fetching html from '+ link +' ...'
        html = gethtml(link)
        if html=='' or html == 'None':
            print "Can't get them html from " + link
            continue
        
        try:
            subtree = etree.HTML(html)
            subnodes = subtree.xpath("//td[@class='frame_style_padding']")
        except:
            if debug:
                f = open("log.txt","wa")
                f.write(html)
                print("error to resolve the html " + link)
                sys.exit()
            else:
                continue
            
        for sn in subnodes:
            if debug and total>=10:
                break;
                            
            sls = sn.xpath(".//a")
            for sl in sls:
                if debug and total>=10:
                    break;
                            
                link = prelink + "restaurants/" + sl.get("href")

                print 'Fetching html from '+ link +' ...'                
                html = gethtml(link)
                if  html=='' or html == 'None':
                    print "Can't get them html from " + link
                    continue
                
                try:
                    sstree = etree.HTML(html)
                    ssnodes = sstree.xpath("//table[@width='94%'][@height='80px']")
                except:
                    if debug:
                        f = open("log.txt","wa")
                        f.write(html)
                        f.write("\r\n\r\n")
                        print("error to resolve the html" + link)
                        sys.exit()
                    else:
                        continue
                    
                for ssn in ssnodes:
                    if debug and total>=10:
                       break;
                            
                    #name
                    n = ssn.xpath(".//tr[1]/td[1]/a[1]")
                    name = ''
                    
                    if len(n)>0:
                        name = decodeHtmlEntity(n[0].text)
                        name = name.strip()
                        #print name

                    #address
                    n = ssn.xpath(".//tr[2]/td[1]")

                    #address array                    
                    address_arr =[]                    
                    address = ''
                    state = ''

                    if len(n)>0:
                        address = decodeHtmlEntity(n[0].text)
                        #has many locations
                        
                        if address.strip()=='Various Locations':
                            n = ssn.xpath(".//tr[1]/td[1]/div[1]/span[1]")
                            if len(n)>0:
                                
                               address = decodeHtmlEntity(n[0].text)
                               addrlist = address.split()
                               if len(addrlist)>4:
                                    state = addrlist[-2]
                                    city = addrlist[-3]
                                    #remove state and city from the address
                                    address = address.replace(state,'')
                                    address = address.replace(city,'')
                                    address = address.replace(addrlist[-1],'')
                                    address = address.strip()
                                    address_arr.append((address,city,state))
                                    

                                    brn = ssn.xpath(".//tr[1]/td[1]/div[1]/span[1]/br")
                                    for n in brn:
                                        address = decodeHtmlEntity(n.tail)
                                        addrlist = address.split()
                                        if len(addrlist)>4:
                                            state = addrlist[-2]
                                            city = addrlist[-3]
                                            #remove state and city from the address
                                            address = address.replace(state,'')
                                            address = address.replace(city,'')
                                            address = address.replace(addrlist[-1],'')
                                            address = address.strip()
                                            address_arr.append((address,city,state))
                                
                            else:
                                address_arr.append(('','',''))
                        else:         
                            addrlist = address.split()
                            if len(addrlist)>3:
                                state = addrlist[-1]
                                city = addrlist[-2]
                                #remove state and city from the address
                                address = address.replace(state,'')
                                address = address.replace(city,'')
                                address = address.strip()
                                address_arr.append((address,city,state))

                    #website
                    website = ''
                    n = ssn.xpath(".//tr[3]/td[1]/a[1]")
                    if len(n)>0:
                        website = decodeHtmlEntity(n[0].text)
                        website = website.strip()


                    if name and len(address)>0:
                        for addr in address_arr:
                             dining = {}
                             dining['name'] = name
                             if addr[0] == 'Various Locations':
                                 dining['address'] = ''
                             else:
                                 dining['address'] = addr[0]
                             dining['city'] = addr[1]
                             dining['state'] = addr[2]
                             dining['country'] = country
                             dining['website'] = website

                             # Avoid duplication
                             if not (dining in dining_db):
                                 dining_db.append(dining)
                                 total = total + 1

                             if debug and total>=10:
                                 break;
                    

                

#Close database link
conn.close()
       
#print and save the final result
import csv
cf = open("scraping_result.csv", "w")
writer = csv.writer(cf)
writer.writerow(['name','address','city','state','country','website'])

for  item in dining_db:
     #print item['name'],item['address'],item['city'],item['state'],item['country'],item['website']
     rlist=[]
     rlist.append(item['name'])
     rlist.append(item['address'])
     rlist.append(item['city'])
     rlist.append(item['state'])
     rlist.append(item['country'])
     rlist.append(item['website'])
     writer.writerow(rlist)

cf.close()


print 'The result has been saved into scraping_result.csv!'

