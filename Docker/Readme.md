


# DOCKER

### Useful links 

> https://runnable.com/docker/python/dockerize-your-python-application

> https://amaysim.engineering/the-3-musketeers-how-make-docker-and-compose-enable-us-to-release-many-times-a-day-e92ca816ef17

> https://serversforhackers.com/s/docker-in-development

> https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/


> ***docker***


> **Container**
```
- running instance with required application. 
- Containers are always created from images. 
- Container could expose ports and volumes to interact with other containers or outer world. 
- Container could be easily killed / removed and re-created again in a very short time.
```

> **Image**
```
- basic element for every container. 
- Uses copy-on-write model. 
- During building images every step is cached and could be reused. 
- Building images could take some time - it depends on particular image. 
- While containers can be started from images very quickly.
```

> **Port**
```
- is a TCP/UDP port in it’s classical meaning. 
- There are a lot of modes for networking in Docker containers, 
- so to make things simpler let’s assume that ports could be exposed to 
 outer world (accessible from host OS) or connected to other containers 
- accessible only from that containers and invisible from outer world.
```

> **Volume**
```
- the best explanation is shared folder. 
- Volume keeps data outside of its container but accessible from this container or other connected containers. 
- Data stored in volumes is persistent.
```

> **Registry**
```
- server that keeps images. 
- Could be compared with git - you can pull image from registry to deploy it locally 
- and you can push locally built images to registry 
- (create new image or update image version on registry). 
- Docker registry application is Open Source app like the main application 
- so you could deploy your private Docker Registry on any server you want
```

> **Docker hub**
```
- is a registry with web-interface. 
- It keeps a lot of Docker images with different software. 
```

- ***docker composer***
> manages Docker containers in a very neat way. 

> It allows multiple Docker commands to be written as a single one, which allows our Makefile to be a lot cleaner and easier to maintain.

- ***make - makefile***
> Make is a cross-platform build tool to test and build software and it is used as an interface between the CI/CD server and the application code.

> A single Makefile per application defines and encapsulates all the steps for testing, building, and deploying that application.

> Having a clean Makefile is key. It helps to understand it quickly and to maintain. Therefore, having some conventions like target vs _target, Pipeline targets, and Pipeline targets really aim to make developers’ life easier.


- ***gettig started with docker***
```
C:\WINDOWS\system32>docker run -i -t --rm ubuntu /bin/bash
root@c61ba2599bbb:/# exit


C:\WINDOWS\system32>docker ps -a
CONTAINER ID        IMAGE                                             COMMAND                  CREATED             STATUS                    PORTS               NAMES
5b9fe6cd227e        ubuntu                                            "/bin/echo 'Hello wo…"   10 hours ago        Exited (0) 10 hours ago     

```

- ***dockerfile***
> FROM — set base image

> RUN — execute command in container

> ENV — set environment variable

> WORKDIR — set working directory

> VOLUME — create mount-point for a volume

> CMD — set executable for container


