FROM python:3.7-slim-stretch
RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential

# Copy app source.
WORKDIR /app/text-service
COPY . .
RUN rm pytest.ini test-requirements.txt run-tests.sh
RUN rm -rf tests

# Install requirements.
RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir /tmp/text-service /tmp/text-service/prom-data
ENV prometheus_multiproc_dir /tmp/text-service/prom-data

# Prepare environment.
EXPOSE 8080
ENV FLASK_DEBUG 0

# Start command.
CMD ["sh", "start.sh"]
