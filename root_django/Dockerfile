FROM python:3.11.9-bullseye

ENV APP_HOME /source
ENV ALLOWED_HOSTS 127.0.0.1,localhost,0.0.0.0
ENV APP_USER appuser

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    # used by django in manage.py compilemessages call
    gettext \
    fonts-noto-color-emoji \
    # used by psql
    libpq-dev \
    python3-dev

RUN groupadd -g 9000 $APP_USER && \
    useradd -r -u 9000 -g $APP_USER $APP_USER

WORKDIR $APP_HOME

COPY requirements.txt /
RUN pip install gunicorn==22.0.0
RUN pip install -r /requirements.txt

COPY . $APP_HOME

ENV PYTHONPATH $PYTHONPATH:$APP_HOME/project

COPY ./services/api.sh /

RUN mkdir -p $APP_HOME/static
RUN chmod -R 755 $APP_HOME && \
    chown -R $APP_USER:$APP_USER $APP_HOME

RUN chmod 755 /api.sh

# USER $APP_USER
# breaks a lot of stuff and not really needed in the local development or tests

ENTRYPOINT ["/api.sh"]
CMD ["--help"]