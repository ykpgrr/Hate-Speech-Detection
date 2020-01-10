## Packaging the application
` $ mvn install`

## Running the application
` $ java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar --sa.logic.api.url=http://localhost:5000 ` 

## Building the container
` $ docker build -f Dockerfile -t $DOCKER_USER_ID/hate-speech-detection-backend . `

## Running the container
``` 
$ docker run -d -p 8080:8080 -e SA_LOGIC_API_URL='http://<container_ip or docker machine ip>:5000' $DOCKER_USER_ID/hate-speech-detection-backend 
```

#### Native docker support needs the Container IP
CONTAINER_IP: To forward messages to the machine learning service container we need to get  its IP. To do so execute:

` $ docker container list`

Copy the id of machine learning  container and execute:

` $ docker inspect <container_id> `

The Containers IP address is found under the property NetworkSettings.IPAddress, use it in the RUN command.

#### Docker Machine on a VM 
Get Docker Machine IP by executing:

` $ docker-machine ip `

Use this one in the command.


## Pushing the container
` $ docker push $DOCKER_USER_ID/hate-speech-detection-backend  `


