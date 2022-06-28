# Final Project Saar Salhov

### My system will save receipts of users by store. the system is running on micro-services in Docker.
## Short video of my project
https://youtu.be/DePas4HnWJQ

## Design
![image](https://user-images.githubusercontent.com/86562519/176251856-72b6eadd-d73c-40df-b587-68595f2a00a6.png)
## Prerequisites

* Linux OS
* python3 for running tests
* pytest library for running tests
* Docker
* Docker-compose

## How To Run:
### Backend + Frontend + Mongo + MySql:
please download the repository to your pc.
To run the entire app please get inside "Final-Project-Saar-Salhov" directory using `cd` and run this command in the shell:

```bash
docker-compose up
```

After docker-compose finished to load, you can run in other terminal `docker ps` to see the containers.

We can see that our backend is running on the localhost in port 8000, you can access it by [click here](http://localhost:8000/docs) or by copy this `http://localhost:8000/docs` to the url in your browser. 
After clicking on the link you will see this page:

![image](https://user-images.githubusercontent.com/86562519/172903521-d22dde16-ab54-436e-b21b-96501bc93081.png)

Also we can see that our frontend is running on the localhost in port 8001, you can access it by [click here](http://localhost:8001/) or by copy this `http://localhost:8001/` to the url in your browser. 
After clicking on the link you will see this page:

![image](https://user-images.githubusercontent.com/86562519/172903581-ce01bf4b-7f5a-462e-947a-d75e30c662ab.png)

In addition, we can see that our DB's Mongo and MySql running on ports 8003 and 8002.

This is the output you should get when running the comman `docker ps`:

![image](https://user-images.githubusercontent.com/86562519/176252930-e112dc8e-d215-482d-972a-d558ba89cdea.png)

All the users saved In MySql, and all the receipts saved in Mongo.

## Tests - Backend
To run tests nevigate to Backend/app directory using `cd` command in your shell, and run `pytest`.

