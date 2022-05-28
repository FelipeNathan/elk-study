FROM python:3

WORKDIR /usr/src/app
RUN echo working on ${PWD}

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./src .

EXPOSE 3000

CMD ["python", "main.py"]