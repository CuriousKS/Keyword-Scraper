FROM python:3.13

WORKDIR /scraper4

COPY  .  /scraper4

RUN pip install -r requirements.txt

CMD ["fastapi","run","scraper4.py"]