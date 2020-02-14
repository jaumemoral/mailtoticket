FROM python:3.7.5-alpine3.10
# El /log es per escriure els logs i el /conf es per posar el fetchmailrc (sense el punt) i el settings_default.py
VOLUME /log
VOLUME /conf
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid "$GROUP_ID" "mailtoticket"
RUN adduser --disabled-password --gecos "" --ingroup "mailtoticket" --no-create-home --home /mailtoticket --uid "$USER_ID" mailtoticket
# Posem el timezone correcte pels logs
RUN apk add tzdata && cp /usr/share/zoneinfo/Europe/Madrid /etc/localtime && echo "Europe/Madrid" >/etc/timezone && apk del tzdata
# Instalem dependencies (a part de la resta de programa, perque aixi fa cache)
WORKDIR /mailtoticket
RUN chown mailtoticket:mailtoticket /mailtoticket/
COPY requirements.txt /mailtoticket/
RUN pip install -r requirements.txt
RUN pip install gunicorn
# Copiem el mailtoticket
COPY filtres /mailtoticket/filtres/
COPY soa /mailtoticket/soa/
COPY img /mailtoticket/img/
COPY *.py /mailtoticket/
# Aixo es perque trobi el settings on l'hem deixat
ENV PYTHONPATH=/conf
USER mailtoticket
EXPOSE 5000
#CMD ["gunicorn","--bind","0.0.0.0:5000","server:app"]
ENV FLASK_APP=server.py
CMD ["flask","run","--host=0.0.0.0"]
