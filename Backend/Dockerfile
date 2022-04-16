FROM python:3.9
COPY . /project
WORKDIR /project/app
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
