FROM python:3.9
RUN apt-get update
COPY . /project
WORKDIR /project/app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
