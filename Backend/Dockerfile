FROM python:3.9
COPY . /project
WORKDIR /project/app
RUN pip3 install -r requirements.txt
EXPOSE 8083
CMD [ "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8083"]


