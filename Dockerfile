FROM python:3.12.0

WORKDIR /wea

RUN python3 -m pip install Flask
RUN pip install requests
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
