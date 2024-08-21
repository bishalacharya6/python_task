import os
import django
import json
from kafka import KafkaConsumer
from django.utils import timezone
import sys 

# Configure Django settings
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_2_kafka.settings')
django.setup()

# Import Django model after setup
from faceembed.models import FaceEmbed

# Set up the Kafka consumer
consumer = KafkaConsumer(
    'face.embed.data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def start_consuming():
    print("Consumer started, waiting for messages...")
    for message in consumer:
        data = message.value
        # Save the message data to the Django model
        FaceEmbed.objects.create(
            age=data['age'],
            emotion=data['emotion'],
            gender=data['gender'],
            timestamp=timezone.now()
        )
        print(f"Received: {data}")

if __name__ == "__main__":
    start_consuming()
