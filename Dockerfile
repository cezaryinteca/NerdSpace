FROM python:3.8-alpine

#instalacja pythona i pip
#RUN apk add python3
#RUN apk add py3-pip

#instalacja modulow wymaganych dla aplikacji
#COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /NerdSpace

#kopiowanie plikow wymaganych dla aplikacji
#COPY app.py /usr/src/app/
add . /NerdSpace

RUN pip install -r requirements.txt

#wskaz port do nasluchiwania
EXPOSE 5000

#uruchom aplikacje
CMD ["python", "app.py", "--host=0.0.0.0"]
