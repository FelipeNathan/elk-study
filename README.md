# elk-study

A project to study about observability

I'm using ELK (Elastic, Logstash, Kibana) to check a small application made in python

## Technologies
- Python 
- Flask
- Elastic Apm (Flask)
- Docker
- Docker Compose
- ELK Stack

## Configuration
All the configurations needed are in files inside the services folder
- ./docker/apm-server/apm-server.yml
- ./docker/elasticsearch/config/elasticsearch.yml
- ./docker/filebeat/config/filebeat.docker.yml
- ./docker/kibana/config/kibana.yml
- ./docker/logstash/pipeline/filebeat.conf

## Application

Start all services in docker-compose.yml file

```bash
$ docker-compose -f ./docker/docker-compose.yml up
```

The application is listening on port 3000
```
http://locahost:3000
```

There are a few endpoints to fill the elastic service
- /home
   - this endpoint will log `Calling /home - Lets goooooo` in elastic and print `Hello world` on screen 
   
- /home/me
   - this endpoint will just print `Hello Felipe` on screen
   
- /error/capture/exception
   - this endpoint will gerenate a `ZeroDivisionError` error and be captured by `apm` service and then print `error captured` on screen

- /error/capture/message
   - this endpoint will capture `handling error` message into the `apm` service and then print `error captured` on screen

- /error/capture/extra
   - this endpoint will put some `extra` info into log and then print `error captured` on screen

- /error/capture/extra2
   - same as /extra, just to test different messages
   
- /error/capture/should/<throw>
   - this endpoint, you can pass "true" or "false" to <throw> param, which will:
      - true: thrown an expcetion, which will be captured by apm service
      - false: will not thrown an exception and will just print `not throwing exception` on screen

- /events/<event_name>
   - <event_name> is optional, this will create a transaction name (span) in elastic


## Kibana
The kibana is listening on port 5601
```
http://localhost:5601
```
