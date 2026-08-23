<b><big>KEYWORD  SCRAPER</big></b>


This Project Scrape Suggested Search From Different Websites For A Given Keyword  <br>
To Run This Project As A Docker Container In Detach Mode Use Following Docker Commands In This Directory:  <br>
```    
       docker build -t scraper4:13 .
       docker run  --name scraper413  -d -p8000:8000  scraper4:13
       docker run --net=container:scraper413 selenium/standalone-firefox:nightly
``` 
<br>
<b>
NOTE: It will take a while before you get your result.<br>
Typically it takes one to three minute to give final output.<br>
But this time may vary depending on internet speed and system hardware.<br>
</b>