# Kafka-Django Project

This project demonstrates the integration of Kafka message queue with a Django web application. It includes a producer that publishes messages to a Kafka topic, and a consumer that listens to the topic and processes the messages.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python latest
- Docker
- Docker Compose

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/kafka-django.git
   ```
2. Create a project directory and navigate to the directory:
   ```
   cd your-directory
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   Note: Make sure to install the specific version of the Kafka Python library mentioned in the `requirements.txt` file, as there is a known bug in the library.
   
4. Set up the environment variables:
   ```
   cp new_kafka_env .env
   ```
   Update the `.env` file with the necessary configuration settings.
5. Start the Docker containers:
   ```
   docker-compose up -d
   ```
   This will start the Kafka and Zookeeper services.
6. Verify the installation:
   - Ensure that the Kafka and Zookeeper containers are running:
     ```
     docker ps
     ```
   - Check if the Kafka topic has been created:
     ```
     docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
     ```

## Usage

1. Run the Django server:
   ```
   python manage.py runserver
   ```
2. Open another terminal and navigate to the `faceembed` app directory:
   ```
   cd faceembed
   ```
3. Run the Kafka producer:
   ```
   python producer.py
   ```
   This will start publishing messages to the Kafka topic.
4. Run the Kafka consumer:
   ```
   python consumer.py
   ```
   The consumer will start listening to the Kafka topic and processing the messages.
5. Access the web interface:
   - Open a web browser and go to `http://127.0.0.1:8000/api/face_embed/`
   - Click the "GET" button to retrieve the JSON response containing the processed messages.
