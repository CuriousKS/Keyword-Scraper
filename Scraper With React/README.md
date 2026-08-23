<b><big>KEYWORD  SCRAPER  WITH REACT FRONTEND</big></b>

Like the parent repository , this project also scrape suggested search from different websites for a given keyword.  <br>
It uses FastAPI & Selenium in backend.<br>
To run the backend on local machine (assuming that docker desktop is running & all python dependencies are installed) 
run following commands in "Backend" directory:
```
$docker run -p8000:8000 -d selenium/standalone-firefox:nightly
```

```
$fastapi run scraper4.py
```
This two commands will allow you to use the API for scraper through SWAGER page:http://localhost:8000/docs . <br>
In order to use the scraper with GUI you need to first install  dependencies & start react. <br>Run following commands in "frontend" directory :
```
$npm install
```
```commandline
npm run dev
```
