# Final Project Saar Salhov - Backend

## Prerequisites

* Linux OS
* python3 for running tests
* pytest library for running tests
* Docker

## How To Run:
Build the Dockerfile using:

```bash
docker build -t backend ./ -f Dockerfile
```
After  the Dockerfile finished to load, run this command to run the container:

```bash
docker run -p8000:8000 backend
```

Now we can see that our server is running on the localhost in port 8000, after the container is up you can access it by [click here](http://localhost:8000/docs) or by copy this `http://localhost:8000/docs` to the url in your browser. 

## Tests
To run tests nevigate to Backend/app directory using `cd` command in your shell, and run `pytest`.

