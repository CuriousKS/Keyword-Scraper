<b><big>KEYWORD  SCRAPER</big></b>


This project scrape suggested search from different websites for a given keyword.  <br>
To run this project as a docker container use following docker commands in this directory:  <br>
```    
       docker build -t scraper4:13 .
       docker run  --name scraper413  -d -p8000:8000  scraper4:13
       docker run --net=container:scraper413 selenium/standalone-firefox
```
To access the HTML based user interface open browser and hit the url (after executing above commands): http://localhost:8000 and to access the swagger page go to : http://localhost:8000/docs


