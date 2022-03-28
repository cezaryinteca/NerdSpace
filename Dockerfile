FROM python:3.8-alpine

WORKDIR /NerdSpace

#kopiowanie plikow wymaganych dla aplikacji
add . /NerdSpace

RUN pip install -r requirements.txt

RUN mkdir -p /tmp
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /srv

ADD main.py /srv
ADD gunicorn_cfg.py /srv
ADD wsgi.py /srv

WORKDIR /srv

ENV GUNICORN_WORKERS=4
ENV prometheus_multiproc_dir=multiproc-tmp

CMD rm -rf multiproc-tmp && \
	mkdir multiproc-tmp && \
	gunicorn -c gunicorn_cfg.py --bind 0.0.0.0:8080 -w $GUNICORN_WORKERS wsgi:app

#wskaz port do nasluchiwania
EXPOSE 5000

#uruchom aplikacje
CMD ["python", "app.py", "--host=0.0.0.0"]
