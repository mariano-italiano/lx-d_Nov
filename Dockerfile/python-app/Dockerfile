FROM python:3.10-slim-buster

LABEL "Application"="Test Python App"
LABEL "Author"="Marcin K."

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && adduser flaskuser

COPY --chown=flaskuser:flaskuser . .
RUN chmod -R 755 .

USER flaskuser

ENV APP_VERSION="1.0"
ENV APP_BRANCH="develop"

CMD ["python3", "app.py"]

