# -*- coding: utf-8 -*-
#from src.__init__ import *
#python  3 需要装bs4 模块， 

import requests
import urllib
import re
import json
import  string
import shutil
import os
from bs4 import BeautifulSoup
from tkinter.constants import PAGES
from itertools import count
from builtins import int, str
from urllib import request
from urllib import parse
#火龙果软件工程文档破解限制10次下载。
#1.先到http://wenku.uml.com.cn注册个账号密码
#2.填写账号密码
#3.更改你需要下载的路径
url = "http://wenku.uml.com.cn";
index = 1
username = "你的用户名"
password = "你的密码"
dowloadpath = "C:/document/"
#创建文件夹
def createfolad(path):
    ps = dowloadpath
    ps = ps + path
    if(False == os.path.exists(ps)):
        os.makedirs(ps)
        print("创建文件夹---->"+ps+"----------------------------->【OK】")
#获得内容页面url
def getMainUrl(urls, i,flag = True):
    tempurl = url
    if(flag == False):
        tempurl = ""
    u =  tempurl+parse.quote(urls.encode('GBK'), safe = string.printable)
    return u[0:len(u)-1]+str(i)
#下载文件进度方法
def file_down_status(a,b,c):
    pel = 100.0*a*b/c
    if pel>100:
       pel = 100
       
#转换下载路径
def getDownloadFilePath(path):
    return url + "/" +str(path)

#转换URL
def getUrl(urls,flag = True):
    tempurl = url 
    if(flag == False):
        tempurl = ""
    return tempurl+parse.quote(urls.encode('GBK'), safe = string.printable)
#登陆获取数据
def sendUrl(urls):
    data = {'username': username,"password":password}
    headers = {
               'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    session=requests.session()
    r = session.post('http://user.uml.com.cn/loginok.asp', data=data, headers=headers)
    response = session.get(urls,headers=headers)
    return response;
#下载内容
def getDownload(urls, foladPath, fileName, serverFileName, floadName,file_ext,child):
     dpath = "E:/document/"+foladPath+"/"
     downloadPath = url+"/document/"+child+"/"+serverFileName
     print("目录定位--->【"+floadName+"】------>开始下载【"+fileName+"】...")
     try:
         request.urlretrieve(getUrl(downloadPath, False),dpath+fileName,file_down_status)
     except:
         if(file_ext == 'docx'):
            downloadPath = downloadPath[0:len(downloadPath)-1]
            fileName = fileName[0:len(fileName)-1]
         if(file_ext == 'ppt'):
            downloadPath = downloadPath + "x"
            fileName = fileName + "x"
         try:
             request.urlretrieve(getUrl(downloadPath, False),dpath+fileName,file_down_status)
         except:
             print(fileName+"下载失败----------------->【ok】")
             return
     print(fileName+"下载成功----------------->【ok】")
  
  
  
  
     #FilePage = sendUrl(urls).content.decode('GBK')
     #tables = BeautifulSoup(FilePage, 'html.parser').find_all('td',{'width':'664','valign':"center",'height':"50"})
     #downloadPath = tables[0].find_all("a",{'target':'_blank'})
     
   #  html = sendUrl(getDownloadFilePath(downloadPath[0]['href'])).content.decode('GBK');
   #  script = BeautifulSoup(html, 'html.parser').find_all('script')
     
     
     #IDEF0建模
   #  r = re.compile("href=\'(.+?)\'");   
   #  ph = r.search(str(script[0])).group(0)
  #   if(ph!=False):
  #       ph = str(ph)[7:len(ph)-1]
  #       print("开始下载文件到【"+dpath+fileName+"】------------->"+getUrl(getDownloadFilePath(ph),False)+".....")
  #       request.urlretrieve(getUrl(getDownloadFilePath(ph),False),dpath+fileName,file_down_status)
  #       print(fileName+"下载成功----------------->【ok】")
#获得列表内容
def getContent(content,foladPath,floadName,child):
    tables = BeautifulSoup(content, 'html.parser').find_all('table',{'cellspacing':'1','cellpadding':'4','class':'content','width':"700"})

    for k in tables[0].find_all('tr'):
        file_ext = k.find_all('img')[0]['src']
        file_ext = file_ext[8:len(file_ext)-4]
        files = k.find_all('a')[0]
        if(file_ext == 'doc'):
            file_ext = 'docx'
        if(file_ext == 'pdf'):
            file_ext = 'pdf'
        serverFileName = str(files.string)+"."+str(file_ext)
        fileName = serverFileName.replace("..",".")
        #调用进入内容页下载
        getDownload(getUrl("/"+files['href']),foladPath, fileName,serverFileName,floadName,file_ext,child)


def getPageSize(content):
    r = re.compile('有(\d+)页');   
    p = r.search(str(content)).group(0)
    return p[1:len(p)-1]

html = sendUrl(url+"/wkpart.asp").content.decode('GBK');
dd = BeautifulSoup(html, 'html.parser').find_all('div',{'id':'menum'})
def depinContent(u, PageSize,floadName):
    urls = u
    pagesize = int(PageSize)
    for i in range(pagesize):
        foladPath = floadName+"/"+str(i+1)
        createfolad(foladPath)
        Content = sendUrl(getMainUrl(urls,i+1,False)).content.decode('GBK')
        #UI
        if(floadName == 'UML'):
          child = "UML"
        if(floadName == '建模'):
            child = "UI"
        if(floadName == '需求'):
            child = "requirement"
        if(floadName == '设计'):
            child = "swdesign"
        if(floadName == '编码、构建与集成'):
            child = "bmgjjc"
        if(floadName == '测试'):
            child = "test"
        if(floadName == '界面'):
            child = "UI"
        if(floadName == '产品管理'):
            child = "productmana"
        if(floadName == '项目管理'):
            child = "xmgl"
        if(floadName == '研发管理'):
            child = "productmana"
        if(floadName == '配置管理'):
            child = "pzgl"
        if(floadName == '质量管理'):
            child = "zlgl"
        if(floadName == '过程改进'):
            child = "process"
        if(floadName == '大数据'):
            child = "bigdata"
        if(floadName == '数据库'):
            child = "datebase"
        if(floadName == '数据仓库'):
            child = "datecangku"
        if(floadName == '数据挖掘'):
            child = "datecangku"
        if(floadName == '企业架构'):
            child = "qiyejiagou"
        if(floadName == 'IT规划与治理'):
            child = "ITguihua"
        if(floadName == '运营管理'):
            child = "yunyinggl"
        if(floadName == 'IT运维'):
            child = "itil"    
        if(floadName == 'DevOps'):
            child = "devops"       
        if(floadName == '安全'):
            child = "safe"         
        if(floadName == 'JAVA'):
            child = "java"      
        if(floadName == '.net'):
            child = "net"     
        if(floadName == 'c,c++'):
            child = "C"         
        if(floadName == 'web开发'):
            child = "web"         
        if(floadName == '移动端开发'):
            child = "phone"                    
        if(floadName == '嵌入式开发'):
            child = "qrskf"       
        if(floadName == 'IT人员培养'):
            child = "itpeiyang"            
        if(floadName == '云计算'):
            child = "yjs"       
        if(floadName == '网络技术'):
            child = "wljs"        
        if(floadName == '办公'):
            child = "office"        
        if(floadName == '人工智能'):
            child = "ai"      
        if(floadName == 'python'):
            child = "python"    
        if(floadName == '微服务'):
            child = "wfw"      
        if(floadName == '学生'):
            child = ""  
            return         
        getContent(Content,foladPath, floadName,child)
  
def main():
    #递归改循环
    for k in dd[0].find_all('a'):
        wenku = sendUrl(getMainUrl(k['href'],1)).content.decode('GBK')
        floadName = k.string.replace("\n","").replace("\r","").replace(" ","")
        createfolad(floadName)
        pageSize = int(getPageSize(BeautifulSoup(wenku, 'html.parser').find_all('div',{'align':'right'})[0]))
        url = getMainUrl(k['href'],1)
        depinContent(url, pageSize, floadName)
        #递归，深度
        #for j in BeautifulSoup(wenku, 'html.parser').find_all('div',{'align':'right'}):  
       #     pageSize = int(getPageSize(j))
       #     if(index < pageSize):
      #          index = index +1
       #         getContent(wenku)
       #     else:
      #          index = 1
      #          continue
       # print(index)
      #  main(index)
        #列表
        #getContent(wenku)
        #for j in BeautifulSoup(wenku, 'html.parser').find_all('div',{'align':'right'}):
        # print(r.search(str(j)).group(0))
main()