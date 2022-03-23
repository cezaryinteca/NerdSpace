FROM alpine:3.5

#instalacja pythona i pip
RUN apk add --update py3-pip

#instalacja modulow wymaganych dla aplikacji
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

#kopiowanie plikow wymaganych dla aplikacji
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

#wskaz port do nasluchiwania
EXPOSE 5000

#uruchom aplikacje
CMD ["python", "/usr/src/app/app.py"]
