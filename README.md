# Final Project Saar Salhov

### My system will save receipts of users by store. the system is running on micro-services in Docker.

## Design
![image](https://user-images.githubusercontent.com/86562519/165363837-bc4a7cd4-b66b-47af-8739-30ab9a1615d1.png)

## Prerequisites

* Linux OS
* python3 for running tests
* pytest library for running tests
* Docker
* Docker-compose

## How To Run:
### Backend + Frontend:
please download the repository to your pc.
To run the Backend and the frontend together please get inside "Final-Project-Saar-Salhov" directory using `cd` and run this command in the shell:

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

## Tests - Backend
To run tests nevigate to Backend/app directory using `cd` command in your shell, and run `pytest`.

