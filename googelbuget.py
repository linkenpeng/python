#coding=utf8
__doc__ = '''
author:leon
email:nickylans@163.com

'''
import re
import os
import urllib2, urllib
import cookielib
from md5 import md5
import pycurl
import stat
import cStringIO as StringIO
from mysql import dbconn
import traceback
import sys, base64,hashlib
import time

def passportDecrypt(txt):
    s = base64.decodestring(txt)
    txt = passportKey(s)
    tmp = u''
    for i in xrange(0, len(txt), 2):
        md5 = txt[i]
        k = i + 1
        if k == len(txt):k = 0
        tmp += unichr(ord(txt[k]) ^ ord(md5))
    return eval(repr(tmp)[1:])

def passportKey(txt, key='fsdjk2rt'):
    md5 = hashlib.md5(key).hexdigest()
    encrypt_key = md5
    ctr = 0
    tmp = u''
    for i in range(len(txt)):
        ctr = 0 if ctr == len(encrypt_key) else ctr
        tmp += unichr(ord(txt[i]) ^ ord(encrypt_key[ctr]))
        ctr += 1
    return tmp


class GoogleLogin(object):
    loginUrl = "https://accounts.google.com/ServiceLogin?service=adwords&hl=zh_CN&ltmpl=regionala&passive=true&ifr=false&alwf=true&continue=https://adwords.google.com/um/gaiaauth?apt%3DNone%26ltmpl%3Dregionala&sacu=1&sarp=1"
    loginAction = "https://accounts.google.com/ServiceLoginAuth"
    bugetUrl = "https://adwords.google.com/select/ManageBudgets"
    cachePath = 'cookie/'
    mccAccount = 'xxxxx@teamtop.com.cn'
    #登陆框正则
    #preg_form = '<form> <\/form>'
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.getCookieFile()
        self.isMcc = self.isMccAccount(username)
        self.isLogin = self._loginPost()
    
    def isMccAccount(self, accountName):
        if accountName == self.mccAccount:
            return True
        else:return False

    def _loginPost(self):
        content = self.getURLContent(self.loginAction)
        postInfo = self.getPostData(content)
        
        cont = self.postToGoogle(postInfo)
        
        if cont.find("captcha-msg") == -1 and cont.find("errormsg_0_Passwd") == -1:
            print "%s login ok" % self.username
            extId = self.getExtId(cont)
            print "extId=",extId
            if extId and int(extId) > 5:
               
                updateExtId(self.username, extId)
            insertLog(self.username, 1)
            #提取extid
            return True #登陆成功
        else:
            print 'can\'t login account %s' % self.username
            insertLog(self.username, 0)
            #raise Exception("Can't login in %s" % self.username)
            return False
        

    def getExtId(self, pagCont):
        rs = re.findall("clientInfo={customerId:'(\d+)'", pagCont.strip())
        if rs:
            return rs[0]

    @staticmethod
    def getFileMd5(fileName):
        md = md5(fileName)
        return md.hexdigest()

    @staticmethod
    def isWrite(fileName):
        num = oct(os.stat(fileName)[stat.ST_MODE ])[-3:]
        if int(num) >= 600:
            return True
        else:
            return False

    def checkCookieFile(self):
        cookieFile = self.cachePath + GoogleLogin.getFileMd5(self.username)
        try:
            open(cookieFile, "w+").close()
        except:
            raise
        self.isWrite(cookieFile)
        if self.isWrite(cookieFile):
            os.remove(cookieFile)
        else:
            raise Exception("%s is can not write" % cookieFile)
    
    def getCookieFile(self):
        self.checkCookieFile()
        return self.cachePath + GoogleLogin.getFileMd5(self.username)

    def getURLContent(self, pageUrl, cookieFile=None):
        if not cookieFile:
            cookieFile = self.cachePath + GoogleLogin.getFileMd5(self.username)
        html = StringIO.StringIO()
        c = pycurl.Curl()
        c.fp = html
        i = 0
        while True:
            try:
                c.setopt(pycurl.URL, pageUrl)
                c.setopt(pycurl.WRITEFUNCTION, html.write)
                c.setopt(pycurl.FOLLOWLOCATION, 1)
                c.setopt(pycurl.MAXREDIRS, 5)
                c.setopt(pycurl.SSL_VERIFYPEER, 0)
                c.setopt(pycurl.COOKIEFILE, cookieFile)
                c.setopt(pycurl.COOKIEJAR, cookieFile)
                c.perform()
                break
            except:
                i = i + 1
                if i >= 20:return
                traceback.print_exc()

        httpCode = c.getinfo(pycurl.HTTP_CODE)
        content = c.fp.getvalue()
        if httpCode != 200: raise Exception("can not get page content")
        return content

    def getPostData(self, content):
        '''
        @content string:
            登陆页面内容
        '''
        #检测登陆页面是否更改，并提取相应的post字段
        cont = content
        rs = re.findall(r'<form[\s\S]*id="gaia_loginform".*?>([\s\S]*)<\/form>', cont.strip(), re.U)
        if not rs:
            raise Exception("目标页面已经更新，请重写正则")
        loginForm = rs[0].strip()
        #print loginForm
        rs = re.findall(r'<input.*?>', loginForm, re.U|re.I|re.S)
        if not rs:
            raise Exception("无法提取输入框，请重写正则")
        postInfo = {}
        for i in rs:
            nv = re.findall(r'name="(.*?)"', i.strip(), re.U|re.I|re.S)
            if nv:
                vl = re.findall(r'value="(.*?)"', i.strip(), re.U|re.I|re.S)
                postInfo[nv[0]] = vl[0] if vl else ''

        if not postInfo:
            raise Exception("出问题了")
        userAndPass = urllib.urlencode({'Email':self.username, 'Passwd':self.password})
        return "continue=https%3A%2F%2Fadwords.google.com%2Fum%2Fgaiaauth%3Fapt%3DNone%26amp%3Bltmpl%3Dregionala%26amp%3Bltmpl%3Dregionala%26amp%3Bltmpl%3Dregionala&service=adwords&ifr=false&dsh="+postInfo['dsh']+"&ltmpl=regionala&hl=zh_CN&alwf=true&sarp=1&GALX="+ postInfo['GALX'] +"&pstMsg=0&dnConn=&checkConnection=&checkedDomains=youtube&timeStmp=&secTok=&signIn=%E7%99%BB%E5%BD%95&PersistentCookie=yes&rmShown=1&"+userAndPass
    
    def postToGoogle(self, postData, postUrl=None, refUrl=None):
        flag = 0
        if not postUrl:
            refUrl = self.loginUrl
            pUrl = self.loginAction
        else:
            flag = 1
            refUrl = refUrl
            pUrl = postUrl
            print postData
            print pUrl
            print refUrl
            #exit()
        cookieFile = self.cachePath + GoogleLogin.getFileMd5(self.username)
        html = StringIO.StringIO()
        c = pycurl.Curl()
        c.fp = html
        c.setopt(pycurl.URL, pUrl)
        c.setopt(pycurl.WRITEFUNCTION, html.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.REFERER, refUrl)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.POSTFIELDS, postData)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.COOKIEFILE, cookieFile)
        c.setopt(pycurl.COOKIEJAR, cookieFile)
        c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.57 Safari/534.24')
        c.perform()
        httpCode = c.getinfo(pycurl.HTTP_CODE)
        cont = c.fp.getvalue()
        if httpCode != 200: raise Exception("can not get page content, httpCode=%s" % httpCode)
        return cont

    def getBugetAndCost(self, bugetUrl=None):
        if self.isLogin == False:return
        pageUrl = self.bugetUrl if None == bugetUrl else bugetUrl
        pageContent = self.getURLContent(pageUrl)
        reg = 'id="budget\.[0-9]+">&yen;([0-9,\.]+).*?<td align="right">([0-9\.]+)%<'
        rs = re.findall(reg, pageContent, re.I|re.U|re.S)
        if rs:
            #存在有效预算与待审批预算，可提取余额
            buget = float(rs[0][0].replace(',', ''))
            cost = float(rs[0][1].replace(',', ''))
            blance = buget - buget * cost/100.0
            return (buget,blance)
        

def getGoogleAccount():
    pass

def updateExtId(username, extId):
    db = dbconn()
    sql = "UPDATE  `topapi`.`google_sms_account` SET  `extid` = '%s' WHERE  `username` = '%s'" % (
        extId, username
    )
    db.execute(sql)

def insertLog(username, result):
    db = dbconn()
    sql = "insert ignore into topapilog.google_simlogin_log (username,result,inserttime)values('%s','%s',NOW())" % (
        username, result
    )
    db.execute(sql)


def getAccountInfo():
    db = dbconn()
    sql = "select a.id as id, a.username as username,a.password as password FROM topapilog.google_simlogin_log b left join  topapi.google_sms_account a ON a.username = b.username where b.result=0"
    rs = db.fetchall(sql)
    if rs:
        return rs

def getBalance(accountInfo):
    time.sleep(0.2)
    db = dbconn()
    username = accountInfo['username']
    try:
        password = passportDecrypt(accountInfo['password'])
    except:
        print 'en fault!'
        return
    print username
    try:
        infos = GoogleLogin(username, password).getBugetAndCost()
    except:
        print 'had error!'
        traceback.print_exc()
        pass
        return
    if not infos:
        print 'not balance'
        return
    balance = infos[1]
    if balance:
        sql = "update `topapi`.`google_sms_account` SET balance=%s WHERE username='%s'" % (balance, username)
        db.execute(sql)

def testAccount():
    db = dbconn()
    sql = "select a.id, a.username,a.password FROM topapilog.google_simlogin_log b left join  topapi.google_sms_account a ON a.username = b.username where b.result=0"
    rs = db.fetchall(sql)
    print len(rs)

if __name__ == '__main__':

    inList = getAccountInfo()
    from WorkerManager import WorkerManager
    wm = WorkerManager(10)
    for i in inList:
        wm.addJob(getBalance, i)
    wm.waitForComplete()
    exit()