FROM python:3.8-alpine3.12
WORKDIR /Selenium-Python
COPY . /Selenium-Python
RUN pip install -r requirements.txt
ENV TZ=Asia/Taipei