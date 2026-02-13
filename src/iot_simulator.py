import random
import time

def generate_iot_data():
    return {
        "traffic": random.choice([0, 1, 2]),
        "temperature": round(random.uniform(18, 40), 2),
        "distance_remaining": round(random.uniform(10, 300), 1)
    }

def stream_iot_data():
    while True:
        yield generate_iot_data()
        time.sleep(2)