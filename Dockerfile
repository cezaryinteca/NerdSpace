FROM python:3.8-alpine

WORKDIR /NerdSpace

#kopiowanie plikow wymaganych dla aplikacji
add . /NerdSpace

RUN pip install -r requirements.txt

RUN mkdir -p /tmp
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /srv

ADD app.py /srv

#wskaz port do nasluchiwania
EXPOSE 5000

#uruchom aplikacje
CMD ["python", "app.py", "--host=0.0.0.0"]