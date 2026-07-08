from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from typing import Annotated

from fastapi.responses import JSONResponse
from fastapi import FastAPI,Depends,FastAPI,HTTPException,Request,status,Form
from fastapi.templating import Jinja2Templates
import time
from datetime import datetime

from csv import DictReader
from tinydb import TinyDB,where

import json as js
from starlette.exceptions import HTTPException as StartletteHTTPException

app=FastAPI()
templates=Jinja2Templates(directory="html_files")

timestamp=''
keyword_=''
result={}
def get_driver():
    '''For working with headless driver'''
    try:
        ops=webdriver.ChromeOptions()                   #1
        print("<<  Line1 Executed Successufully  >>>")
        ops.headless=True                               #2
        print("<<  Line2 Executed Successufully  >>>")
        ops.add_argument("--headless=new")              #3
        ops.add_argument("--window-position=-2400,-2400")
        print("  <<Line3 Executed Successufully  >>>")
        browser = webdriver.Chrome(options=ops)         #4
        print("<< Line4 Executed Successufully  >>>")
        browser.implicitly_wait(10)                     #5
        print("<<  Line5 Executed Successufully  >>>")
        return browser
    except:
        return -1


def get_driver2():
    try:
        ops=webdriver.ChromeOptions()
        browser = webdriver.Chrome(options=ops)
        browser.implicitly_wait(10)                     
        return browser
    except:
        return -1


def get_driver3():
    ''' For Working With selenium/standalone-chrome '''
    try:
        browser=webdriver.Remote(  "http://localhost:4444",options=webdriver.ChromeOptions()   )
        return browser
    except:
        return -1

def get_driver4():
    ''' For Working With selenium/standalone-firefox '''
    try:
       browser=webdriver.Remote(  "http://localhost:4444",options=webdriver.FirefoxOptions()   )
       return browser
    except:
        return -1


@app.get('/')
def f0(request:Request):
    return templates.TemplateResponse(request,"home.html")
   
#@app.get('/scraper/google_scraper/{x}')
def f1(x:str):
    driver = get_driver4()
    if driver==-1:
        output = "Unknown ERROR Occured!\nWebdriver couldn't configuredd!.\nCheck your internet connection & try again later"
        raise HTTPException(status_code=503,detail = output)
    else:
        try:
            driver.get('https://www.google.com')
            e1=driver.find_element(By.XPATH,"//textarea[@title='Search']")
            e1.send_keys(x)
            time.sleep(6)
            e1=driver.find_elements(By.XPATH,"//div[@role='presentation' and @class='wM6W7d']//span")
            output=list()
            for i in e1:
                output.append(i.text)
        except:
            output = "ERROR: Failed to connect to google!"
            driver.quit()
            #print(output)
            raise HTTPException(status_code=503,detail = output) 
        else:
            if(len(output))==0:
                print("> No data from google.\n")
                output=["<< Unable to fetch data from google >>"]
            else:
                print("> Data have been successfully fetched from google.\n")
                      
        driver.quit()    
        return output

        
#@app.get('/scraper/duckduckgo_scraper/{x}')
def f2(x:str):
    driver = get_driver4()
    if driver==-1:
        output = "Unknown ERROR Occured!\nWebdriver couldn't configuredd!.\nCheck your internet connection & try again later"
        raise HTTPException(status_code=503,detail = output)
    else:
        try:
            driver.get('https://duckduckgo.com')
            e2=driver.find_element(By.XPATH,"//input[@id='searchbox_input']")
            e2.send_keys(x)
            time.sleep(6)
            e2=driver.find_elements(By.XPATH,"//span[@class='react-aria-Text' or @slot='label']")
            output=[]
            for i in e2:
                output.append(i.text)
        except:
            output = "ERROR: Failed to connect to duckduckgo!"
            driver.quit()
            raise HTTPException(status_code=503,detail = output) 
        else:
            if(len(output))==0:
                print("> No data from duckduckgo.\n")
                output=["<< Unable to fetch data from duckduckgo >>"]
            else:
                print("> Data have been successfully fetched from duckduckgo.\n")
                      
        driver.quit()    
        return output


#@app.get('/scraper/bing_scraper/{x}')
def f3(x:str):
    
    '''This scraper won't work in headless mode.'''
    driver = get_driver4()
    if driver==-1:
        output = "Unknown ERROR Occured!\nWebdriver couldn't configuredd!.\nCheck your internet connection & try again later"
        raise HTTPException(status_code=503,detail = output)
    else:
        try:
            driver.get('https://bing.com')
            e3=driver.find_element(By.XPATH,"//textarea[@type='search']")
            e3.send_keys(x)
            time.sleep(6)
            e3=driver.find_elements(By.XPATH,"//ul[@role='listbox']//li")
            output=[]
            for i in e3:
                output.append(i.text)
        except:
            output = "ERROR: Failed to connect to bing!"
            driver.quit()
            raise HTTPException(status_code=503,detail = output) 
        else:
            if(len(output))==0:
                print("> No data from bing.\n")
                output=["<< Unable to fetch data from bing >>"]
            else:
                print("> Data have been successfully fetched from bing.\n")
                      
        driver.quit()    
        return output


#@app.get('/scraper/youtube_scraper/{x}')
def f4(x:str):
    driver = get_driver4()
    if driver==-1:
        output = "Unknown ERROR Occured!\nWebdriver couldn't configuredd!.\nCheck your internet connection & try again later"
        raise HTTPException(status_code=503,detail = output)
    else:
        try:
            driver.get('https://www.youtube.com')
            e4=driver.find_element(By.XPATH,"//input[@name='search_query']")
            e4.click()
            e4.send_keys(x)
            time.sleep(6)
            e4=driver.find_elements(By.XPATH,"//div[@role='option'  and   @aria-label]")
            output=[]
            for i in e4:
                output.append(i.text)
        except:
            output = "ERROR: Failed to connect to youtube!"
            driver.quit()
            raise HTTPException(status_code=503,detail = output) 
        else:
            if(len(output))==0:
                print("> No data from youtube.\n")
                output=["<< Unable to fetch data from youtube >>"]
            else:
                print("> Data have been successfully fetched from youtube.\n")
                      
        driver.quit()    
        return output


#@app.get('/scraper/ebay_scraper/{x}')
def f5(x:str):
    driver = get_driver4()
    if driver==-1:
        output = "Unknown ERROR Occured!\nWebdriver couldn't configuredd!.\nCheck your internet connection & try again later"
        raise HTTPException(status_code=503,detail = output)
    else:
        try:
            driver.get('https://www.ebay.com')
            print()
            e5=driver.find_element(By.XPATH,"//input[@title='Search']")
            e5.click()
            e5.send_keys(x)
            time.sleep(6)
            e5=driver.find_elements(By.XPATH,"//span[@class='ebay-autocomplete-suggestion']")
            output=[]
            for i in e5:
                output.append(i.text)
        except:
            output = "ERROR: Failed to connect to ebay!"
            driver.quit()
            raise HTTPException(status_code=503,detail = output) 
        else:
            if(len(output))==0:
                print("> No data from ebay.\n")
                output=["<< Unable to fetch data from ebay >>"]
            else:
                print("> Data have been successfully fetched from ebay.\n")
                      
        driver.quit()    
        return output


@app.post('/scraper')
def f6(request:Request,keyword=Form(...)):
    global result
    global timestamp
    global keyword_
    
    keyword_ = keyword
    x1,x2=str(datetime.now()).split()
    timestamp='Date:'+ x1 + '_' + 'Time:' + x2
    L1={"google":True,"duckduckgo":True,"bing":True,"youtube":True,"ebay":True}
    if L1['google']:
        try:
           result['Google'] = f1(keyword)
        except:
            result['Google']=["<<Couldn't Scrape Data From Google!>>"]
       
    if L1['duckduckgo']:
        try:
           result['DuckduckGO'] = f2(keyword)
        except:
            result['DuckduckGO']=["<<Couldn't Scrape Data From DuckduckGO!>>"]


    if L1['bing']:
        try:
           result['Bing'] = f3(keyword)
        except:
            result['Bing']=["<<Couldn't Scrape Data From Bing!>>"]

    if L1['youtube']:
        try:
           result['YouTube'] = f4(keyword)
        except:
            result['YouTube']=["<<Couldn't Scrape Data From YouTube!>>"]

    if L1['ebay']:
        try:
           result['Ebay'] = f5(keyword)
        except:
            result['Ebay']=["<<Couldn't Scrape Data From Ebay!>>"]
       
    print(result)
    return templates.TemplateResponse(request,"result.html",{"result":result,"timestamp":timestamp})     


@app.post('/scraper/saveToDB') 
def f7(request:Request,saveToDB=Form(...)):
    if saveToDB in ('y','Y'):          
            data = {
                    'keyword':keyword_,
                    'datetime':str(timestamp),
                        'scraped_data' :[
                        {'Google':[ result.get('Google',None) ]},
                        {'DuckDuckGO':[ result.get('DuckduckGO',None) ]},
                        {'Bing':[ result.get('Bing',None) ]},
                        {'YouTube':[ result.get('YouTube',None) ]},
                        {'Ebay':[ result.get('Ebay',None) ]}
                                        ]
                    }
            
            with TinyDB("scraper_db.json",indent=4) as db:
                    table=db.table(name="scraped_data")
                    table.insert(data)
    
           
            message = 'Your Scraped Data Have Been Saved Successfully!'
            status_code="201"
            title=status.HTTP_201_CREATED
    else:
        message='Your Scraped Data Have Been Discarded!'
        status_code="204"
        title=status.HTTP_204_NO_CONTENT
    
    
    return templates.TemplateResponse(request,"message.html",{"message":message})


@app.get('/db')
def f8(request:Request):
    with open("scraper_db.json","r") as db:
        message=js.load(db)
        
    return templates.TemplateResponse(request,"db_output.html",
               {"message":message,'status_code':200})
            
 
@app.get("/db/delete/{keyword}/{datetime}")
def f9(request:Request,keyword:str,datetime:str):
    with TinyDB("scraper_db.json",indent=4) as db:
         table=db.table(name="scraped_data")
         table.remove(where('keyword')==keyword and where('datetime') == datetime)
    return templates.TemplateResponse(request,"message.html",
               {"message":"Keyword  '"+str(keyword)+"'  With Timestamp:  "+str(datetime) +" have been deleted successfully",'status_code':'204'})

      
@app.exception_handler(StartletteHTTPException)
def general_http_exception_handler(request:Request,exception:StartletteHTTPException):
    message=(exception.detail if exception.detail
             else "An error occurred. Please check your request & try again")
    
    return templates.TemplateResponse(request,"message.html",
               {"message":message,'status_code':status.HTTP_400_BAD_REQUEST})

      