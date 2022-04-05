FROM python:3.9.5-slim

RUN mkdir -p /home/app

# create the app user
RUN addgroup app && adduser --system --no-create-home app --ingroup app

# create the appropriate directories
ENV HOME=/home/app

ENV APP_HOME=/home/app/

WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Create Other Needed Directories
RUN mkdir -p $APP_HOME/media

RUN mkdir -p $APP_HOME/logs

RUN mkdir -p $APP_HOME/static

#RUN chmod +x $APP_HOME/entrypoint.sh

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt $APP_HOME

RUN pip install -r requirements.txt



# Copy Code Files
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

CMD python manage.py runserver 1000


















# FROM python:3.9.5-slim

# ENV PYTHONBUFFERED 1

# RUN mkdir /code

# WORKDIR /code

# COPY requirements.txt /code/

# RUN pip install --user -r requirements.txt

# COPY ./code

# CMD python manage.py runserver

# # RUN apt-get update && apt-get install -y python3-pip



# COPY . /app

# WORKDIR /app

# CMD ["python", "app.py"]

# EOF

# docker build -t multiform .

# docker run -p 5000:5000 multiform