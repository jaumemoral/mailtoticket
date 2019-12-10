FROM python:3.7.5-alpine3.10
# El /log es per escriure els logs i el /conf es per posar el fetchmailrc (sense el punt) i el settings_default.py
VOLUME /log
VOLUME /conf
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid "$GROUP_ID" "mailtoticket"
RUN adduser --disabled-password --gecos "" --ingroup "mailtoticket" --no-create-home --home /mailtoticket --uid "$USER_ID" mailtoticket
# Instalem fetchmail
RUN apk add fetchmail
COPY docker/fetchmail.sh /mailtoticket/
# Copiem el mailtoticket
COPY filtres /mailtoticket/filtres/
COPY soa /mailtoticket/soa/
COPY *.py requirements.txt /mailtoticket/
RUN chown mailtoticket:mailtoticket /mailtoticket/
WORKDIR /mailtoticket
RUN pip install -r requirements.txt
# Aixo es perque trobi el settings on l'hem deixat
ENV PYTHONPATH=/conf
USER mailtoticket
CMD ["/bin/sh","/mailtoticket/fetchmail.sh"]
