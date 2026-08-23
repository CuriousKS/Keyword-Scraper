from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from typing import Annotated

from fastapi.responses import JSONResponse
from fastapi import FastAPI,Depends,FastAPI,HTTPException,Request,status,Form,Response
from fastapi.templating import Jinja2Templates
import time
from datetime import datetime

from csv import DictReader
#import pandas as pd
from tinydb import TinyDB,where,Query

import json as js
import copy
from starlette.exceptions import HTTPException as StartletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


templates=Jinja2Templates(directory="html_files")

from fastapi.middleware.cors import CORSMiddleware

def get_driver4():
    ''' For Working With selenium/standalone-firefox '''
    try:
       browser=webdriver.Remote(  "http://localhost:4444",options=webdriver.FirefoxOptions()   )
       return browser
    except:
        return -1

   
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
                output=[" "]
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
                output=[" "]
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
                output=[" "]
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
                output=[" "]
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
                output=[" "]
            else:
                print("> Data have been successfully fetched from ebay.\n")
                      
        driver.quit()    
        return output

'''
@app.get('/',status_code=200)
def g0(request:Request):
    return templates.TemplateResponse(request,"home.html")
'''

timestamp=''
keyword_=''
result=dict()
L1={"Google":f1,"DuckDuckGo":f2,"Bing":f3,"YouTube":f4,"Ebay":f5}
@app.get('/scraper')
def g1(request:Request,keyword:str):
    keyword.replace(" ","")
    print("Executing g1...")
    global result
    global timestamp
    global keyword_
    global L1
     
    keyword_ = keyword
    result=dict()
    x1,x2=str(datetime.now()).split()
    timestamp='Date:'+ x1 + '_' + 'Time:' + x2    
    for i in L1:        
            try:
               result[i] = L1[i](keyword)
            except:
                result[i]=[' ']
                
    a=0
    for i in result:
        if len(result[i])>a:
            a=len(result[i])
    
    temp=copy.deepcopy(result)
    for i in temp:
        while( len(temp[i]) <a):
            temp[i].append(' ')
            
    #return temp #For API
    df=pd.DataFrame(temp)
    e=L1.keys()
    e=list(e)
    print(e)
    #return templates.TemplateResponse(request,"result.html",{"df":df,"timestamp":timestamp,"a":a,"L1":L1})
    #return temp
    print({"websites":e,"max_row":a,"data":temp})
    return {"websites":e,"max_row":a,"data":temp}


@app.post('/scraper/saveToDB',response_model=dict,status_code=201) 
def g2(request:Request,response:Response):
    print("Executing g2...")
    print("Saver running...")
    global result
    if len(result)>0:
            print("Saving...")
            data = {
                    'keyword':keyword_,
                    'datetime':str(timestamp),
                        'scraped_data' :[result]}
                                                                                                
            with TinyDB("scraper_db.json",indent=4) as db:
                    table=db.table(name="scraped_data")
                    table.insert(data)
               
            message="Last Scraped Data Have Been Saved Successfully!"
            response.status_code=status.HTTP_201_CREATED
            
    else:
        message="No Data To Save!"
        response.status_code=status.HTTP_204_NO_CONTENT
        
    result=dict()
    print(message)
    return {"message":message} #FOR API
    #return templates.TemplateResponse(request,"message.html",{"message":message})


@app.get('/db',status_code=200)
def g3(request:Request):
    print("Executing g3...")
    global result
    result=dict()
    with open("scraper_db.json","r") as db:
        message=js.load(db)
    
    x = copy.deepcopy(message["scraped_data"])
    for i in x:
        temp=copy.deepcopy(message["scraped_data"][i])
        del message["scraped_data"][i]
        message["keyword: "+temp["keyword"]+" "+temp["datetime"]] = temp['scraped_data'][0]
        
    del message['scraped_data']
    print(message)
    return [message]
            
 
@app.delete("/db/delete/{keyword}/{datetime}",status_code=204)
def g4(request:Request,response:Response,keyword:str,datetime:str):
    print("Executing g4...")
    global result
    result=dict()
    x=Query()
    with TinyDB("scraper_db.json",indent=4) as db:
         table=db.table(name="scraped_data")
         query_response=table.get(x.keyword==keyword and x.datetime==datetime)
         print("query_response = ",query_response)
         if(len(query_response)==0):
             response.status_code=404
             print(f"{keyword} {datetime} is not present in database")
         else:
            table.remove(where('keyword')==keyword and where('datetime') == datetime)
            print(f"Successfully deleted {keyword} {datetime}!")
             
#     return templates.TemplateResponse(request,"message.html",
#                {"message":"Keyword  '"+str(keyword)+"'  With Timestamp:  "+str(datetime) +" have been deleted successfully",'status_code':'204'})

  
@app.exception_handler(StartletteHTTPException)
def general_http_exception_handler(request:Request,exception:StartletteHTTPException):
    print("Executing general_http_exception_handler...")
    global result
    message=(exception.detail if exception.detail
             else "An error occurred. Please check your request & try again")
    
    return templates.TemplateResponse(request,"message.html",
               {"message":message,'status_code':status.HTTP_400_BAD_REQUEST})
