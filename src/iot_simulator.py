import random
import time

def generate_iot_data():
    traffic = random.choices(
        population=[0, 1, 2],
        weights=[0.3, 0.5, 0.2]
    )[0]

    temperature = round(random.uniform(18, 40), 2)

    distance_remaining = round(random.uniform(10, 300), 1)

    humidity = round(random.uniform(40, 95), 1)

    vibration_level = round(random.uniform(0.1, 5.0), 2)

    return {
        "traffic": traffic,
        "temperature": temperature,
        "distance_remaining": distance_remaining,
        "humidity": humidity,
        "vibration": vibration_level
    }

def stream_iot_data(interval=2):
    while True:
        yield generate_iot_data()
        time.sleep(interval)