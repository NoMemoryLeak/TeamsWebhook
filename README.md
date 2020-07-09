# TeamsWebhook

You should have to create your MST Teams Incomming WebHook

## Install
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install curl
sudo apt-get install flask
sudo apt-get install requets

sudo apt-get update
```

You will need to install docker and connect you thanks to
```
sudo docker login
```

## Running Test Locally 

Download file src and open a first Terminal

```
cd <path>/src
python3 app.py
```

Open a second Terminal :
```
    export TEAMS="<your webhook url>"
    curl -XPOST -d '{"title":"<your title>"} -H "Content-type:application/json" http://localhost:8080
```

Open Teams and check your WebHook with your JSOn title

## Running with Docker

 ##### 1- Create a docker image and run it 
```
    sudo docker build -t <user name>/teamsapp .
    sudo docker images
    sudo docker run -p 8080:8080 --env TEAMS="<your webhook url"> <docker user name>/teamsapp
```
 ##### 2- Launch your JSON to Teams

```
    curl -XPOST -d '{"title":"<your title>"} -H "Content-type:application/json" http://localhost:8080
```

### Support

We would love your feedback on this tool so don't hesitate to let us know what is wrong and how we could improve it, just file an [issue](https://github.com/NoMemoryLeak/teamswebhook/issues/new)

### Code of Conduct

This plugin is by no means part of [CNCF](https://www.cncf.io/) but we abide by its [code of conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)
