FROM python:3.8-alpine

WORKDIR /NerdSpace

#kopiowanie plikow wymaganych dla aplikacji
add . /NerdSpace

RUN pip install -r requirements.txt

#wskaz port do nasluchiwania
EXPOSE 5000

#uruchom aplikacje
CMD ["python", "app.py", "--host=0.0.0.0"]
