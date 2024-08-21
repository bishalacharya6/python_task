import random
from datetime import datetime
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

emotions = ["happy", "sad", "angry", "neutral"]
genders = ["male", "female", "other"]

def generate_random_data():
    return {
        "age": random.randint(1, 100),
        "emotion": random.choice(emotions),
        "gender": random.choice(genders),
        "timestamp": int(datetime.now().timestamp())
    }

def send_data_to_kafka():
    for _ in range(10):  # Generate and send 10 messages
        data = generate_random_data()
        future = producer.send('face.embed.data', value=data)
        try:
            record_metadata = future.get(timeout=10)
            print(f"Sent: {data} to partition {record_metadata.partition} at offset {record_metadata.offset}")
        except Exception as e:
            print(f"Error sending message: {e}")

if __name__ == "__main__":
    try:
        send_data_to_kafka()
    finally:
        producer.close()
