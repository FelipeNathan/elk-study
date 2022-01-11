FROM python:3

WORKDIR /usr/src/app
RUN echo working on ${PWD}

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./src .

ENV APM_SERVER_PATH=apm-server:8200

LABEL "app.name"="elk-study"

EXPOSE 3000

CMD ["python", "main.py"]