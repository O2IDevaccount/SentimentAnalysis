# lightweight python
FROM python:3.8-slim-buster

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies
RUN pip install numpy==1.19.2 pandas==1.2.1 seaborn==0.11.0 nltk==3.5 sklearn==0.22.2 Flask==1.1.1 gunicorn==20.0.4 healthcheck==1.3.3 google-cloud-logging==1.15.0

# Run the flask service on container startup
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 SAGunicorns:app
