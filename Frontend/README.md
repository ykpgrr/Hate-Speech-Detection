# NodeJS and NPM install on your computer and then:

`npm install`

# This downloads all the Javascript dependencies of the React application and places them in the folder node_modules and then,

`npm start`


## Building the container
` $ docker build -f Dockerfile -t $DOCKER_USER_ID/hate-speech-detection-frontend . `

## Running the container
` $ docker run -d -p 80:80 $DOCKER_USER_ID/hate-speech-detection-frontend `

## Pushing the container
` $ docker push $DOCKER_USER_ID/hate-speech-detection-frontend `