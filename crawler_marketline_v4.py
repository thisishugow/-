#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:23:40 2020

@author: hugo
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
f=open('Configuration.txt','r',encoding='utf-8') #'r' for read the file
s=f.readlines()
f.close()
mktline = webdriver.Chrome(executable_path=s[2].strip('\n'))
mktline.maximize_window()
mktline.get('https://advantage.marketline.com/Deals/Dashboards')




  

#################################################################################################     
################################Paste the url here###############################################    
biopage=s[0].strip('\n') 
#################################################################################################
################################################################################################# 
mktline.get(biopage)
sleep(7)   

elem = mktline.find_element_by_xpath("//*")
html = elem.get_attribute("outerHTML")
soup = BeautifulSoup(html, 'html.parser')

pages=int(soup.find('span',{'id':'totalbottomPageBox'}).string)
if pages>2100:
    pages=2100
pagecounter=int(s[3].strip('\n'))  #default is 1. Record the latest downloaded page.
ProgressCounter = tqdm(total=pages-pagecounter+1)
inputpage=mktline.find_element_by_xpath('/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/input')
inputpage.send_keys(Keys.BACKSPACE)
inputpage.send_keys(str(pagecounter))
gotobutton=mktline.find_element_by_xpath('/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div/input')
gotobutton.click()  

sleep(3)




annouceddate=[]
headline=[]
completeyear=[]
dealcountry=[]
dealtype=[]
dealsubtypel1=[]
dealsubtypel2=[]
dealsubtypel3=[]
dealsubcategory=[]
dealvalue=[]
aquireinvestor=[]
issuer=[]
status=[]
acquiredstake=[]


try: 
    x=pages-pagecounter+1
    for i in range(x):
        selectcolumn=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/a[1]')
        selectcolumn.click()
        sleep(1)
        selectcolumn_completeyear=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[3]')
        selectcolumn_completeyear.click()
        selectcolumn_status=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[2]')
        selectcolumn_status.click()
        selectcolumn_acquiredstake=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[5]')
        selectcolumn_acquiredstake.click()
        selectcolumn_dealcountry=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[9]')
        selectcolumn_dealcountry.click()
        selectcolumn_dealSubtypeL1=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[11]')
        selectcolumn_dealSubtypeL1.click()
        selectcolumn_dealSubtypeL2=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[12]')
        selectcolumn_dealSubtypeL2.click()
        selectcolumn_dealSubtypeL3=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[13]')
        selectcolumn_dealSubtypeL3.click()
        selectcolumn_dealSubCategory=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/input[14]')
        selectcolumn_dealSubCategory.click()
        
        additall=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/img[2]')
        additall.click()
        applythechange=mktline.find_element_by_xpath(
            '/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/a')
        applythechange.click()
        sleep(1)
        elem = mktline.find_element_by_xpath("//*")
        html = elem.get_attribute("outerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        
        
        AnnoucedDate=soup.find_all('td',{'class':"clsrow",
                                         'data-title':"Announced Date", 
                                         'desc':"Announced", 
                                         'isvisible':"1"})
        
        for i in range(len(AnnoucedDate)):
            try:
                annouceddate.append(AnnoucedDate[i].string.strip().strip('\n'))
            except:
                annouceddate.append('-')
        
        Headline=soup.find_all('td',{'data-title':"Headline",'class':"cssoverflow"})
        for i in range(0,len(Headline)):
            try:
                headline.append(Headline[i].find('a',{'class':"title_a"}).string.strip().strip(';'))
            except:
                headline.append('NA')
        Status=soup.find_all('td', {'data-title':'Status'})
        for i in range(len(Status)):
            try:
                status.append(Status[i].string.strip().strip(';').strip('\n'))
            except:
                status.append('-')



        CompleteYear=soup.find_all('td', {'data-title':"Completed Year"})
        for i in range(len(CompleteYear)):
            try:
                completeyear.append(CompleteYear[i].string)
            except:
                completeyear.append('NA')
        AcquiredStake=soup.find_all('td',{'data-title':'Acquired Stake (%)'})
        for i in range(len(AcquiredStake)):
            try:
                acquiredstake.append(AcquiredStake[i].string)
            except:
                acquiredstake.append('NA')
        
        
        DealCountry=soup.find_all('td',{'data-title':"Deal Country(s)"})
        for i in range(len(DealCountry)):
            try:
                dealcountry.append(DealCountry[i].string)
            except:
                dealcountry.append('NA')
        
        DealType=soup.find_all('td',{'data-title':"Deal Type"})
        for i in range(len(DealType)):
            try:
                dealtype.append(DealType[i].string)
            except:
                dealtype.append('NA')
        
        
        DealSubTypeL1=soup.find_all('td',{'data-title':"Deal SubtypeLevel1"})
        for i in range(len(DealSubTypeL1)):
            try:
                dealsubtypel1.append(DealSubTypeL1[i].string)
            except:
                dealsubtypel1.append('NA')
        
        DealSubTypeL2=soup.find_all('td',{'data-title':"Deal SubtypeLevel2"})
        for i in range(len(DealSubTypeL2)):
            try:
                dealsubtypel2.append(DealSubTypeL2[i].string)
            except:
                dealsubtypel2.append('NA')
        
        DealSubTypeL3=soup.find_all('td',{'data-title':"Deal SubtypeLevel3"})
        for i in range(len(DealSubTypeL3)):
            try:
                dealsubtypel3.append(DealSubTypeL3[i].string)
            except:
                dealsubtypel3.append('NA')
        
        
        DealSubCategory=soup.find_all('td',{'data-title':"Deal Sub-Category"})
        for i in range(len(DealSubCategory)):
            try:
                dealsubcategory.append(DealSubCategory[i].string)
            except:
                dealsubcategory.append('NA')
        
        
        DealValue=soup.find_all('td',{'data-title':"Deal Value(US$m)"})
        for i in range(len(DealValue)):
            try:
                dealvalue.append(DealValue[i].string)
            except:
                dealvalue.append('NA')
        
        
        AquireInvestor=soup.find_all('td',{'data-title':"Acquirer/ Investor"})
        for i in range(len(AquireInvestor)):
            try:
                    
                if AquireInvestor[i].find('a').string!=None:
                    aquireinvestor.append(AquireInvestor[i].find('a').string.strip())
                   
                    
                else:
                    aquireinvestor.append(AquireInvestor[i].find('span').find('a').string.strip().strip(';'))
                    
            except:
                if "<!--!{investor2.Name.Replace" in str(AquireInvestor[i]):
                    #print(str(AquireInvestor[i]))
                    aquireinvestor.append(str(AquireInvestor[i]).strip("""<td data-title="Acquirer/ Investor" class="cssoverflow" desc="Acquirer / Investor" isvisible="1"><!-- Expects IEnumerable<CompanyUrlViewModel> as parameter.   -->""").strip('\n').strip().strip("<!--!{investor2.Name.Replace(\"%X92\", \"\'\")}-->").strip('</td>').strip().strip('\n').strip())
                else:    
                    aquireinvestor.append('NA')
        
       
        
        
        Issuer=soup.find_all('td',{'data-title':"Issuer/Partner/Target"})
        for i in range(len(Issuer)):
            try:

                    
                if Issuer[i].find('a').string!=None:
                    issuer.append(Issuer[i].find('a').string.strip())
                    
                    
                else:
                    issuer.append(Issuer[i].find('span').find('a').string.strip().strip(';'))
                    
                    
            except:
                if "<!--!{investor2.Name.Replace" in str(Issuer[i]):
                    #print(str(Issuer[i]))
                    issuer.append(str(Issuer[i]).strip("""<td class="cssoverflow" data-title="Issuer/Partner/Target" desc="Issuer / Partner / Target" isvisible="1"><!-- Expects IEnumerable<CompanyUrlViewModel> as parameter.   -->""").strip('\n').strip().strip("<!--!{investor2.Name.Replace(\"%X92\", \"\'\")}-->").strip('</td>').strip().strip('\n').strip())
                else:
                    issuer.append('NA')
        
        
        
        ProgressCounter.update(1)
        try:
            if pagecounter==1:
                nextpage=mktline.find_element_by_xpath('/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/a')
            else:
                nextpage=mktline.find_element_by_xpath('/html/body/div[4]/main/div[3]/div[4]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/a[2]')
            nextpage.click()
            pagecounter=pagecounter+1
        except:
            print('Done.')
        sleep(3)
    
    

    
    
    
    
    
    
    data=pd.DataFrame({'Announced Date':annouceddate,
                       "Issuer/Partner/Target":issuer,
                       'Acquirer/ Investor':aquireinvestor,
                       'Headline':headline,
                       'Complete Year':completeyear,
                       'Status':status,
                       'Acquired Stake(%)':acquiredstake,
                       'Deal Country':dealcountry,
                       'Deal Type':dealtype,
                       'Deal subtypeL1':dealsubtypel1,'Deal subtypeL2':dealsubtypel2,'Deal subtypeL3':dealsubtypel3,
                       'Deal Subcategory':dealsubcategory,
                       'Deal Value':dealvalue})
    file_name=s[1].strip('\n')
    data.to_excel(file_name,index=False)  


except Exception as e:
    
    data=pd.DataFrame({'Announced Date':annouceddate,
                       "Issuer/Partner/Target":issuer,
                       'Acquirer/ Investor':aquireinvestor,
                       'Headline':headline,
                       'Complete Year':completeyear,
                       'Status':status,
                       'Acquired Stake(%)':acquiredstake,
                       'Deal Country':dealcountry,
                       'Deal Type':dealtype,
                       'Deal subtypeL1':dealsubtypel1,'Deal subtypeL2':dealsubtypel2,'Deal subtypeL3':dealsubtypel3,
                       'Deal Subcategory':dealsubcategory,
                       'Deal Value':dealvalue})
    file_name=s[1].strip('\n')
    data.to_excel(file_name,index=False)
    print(e)
    print('The download stopped at page',pagecounter,'.\nThe download is not done yet. Something went wrong.')



























