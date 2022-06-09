# Final Project Saar Salhov - Frontend

## Prerequisites

* Linux OS
* Docker

## How To Run:
Build the Dockerfile using:

```bash
docker build -t frontend ./ -f Dockerfile
```
After  the Dockerfile finished to load, run this command to run the container:

```bash
docker run -p 8001:3000 frontend
```

Now we can see that our web page is running on the localhost in port 8001, after the container is up you can access it by [click here](http://localhost:8001/) or by copy this `http://localhost:8001/` to the url in your browser. 


