import os
import time
import json
import random
from datetime import datetime
import redis

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
SENSOR_ID = os.getenv('SENSOR_ID', 'rbt-01')

if not REDIS_PASSWORD:
    print('ERROR: REDIS_PASSWORD not set')
    raise SystemExit(1)

def connect():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

def produce_loop():
    r = connect()
    while True:
        try:
            valor = round(random.uniform(0, 100), 2)
            timestamp = datetime.now().isoformat()
            payload = {"sensor_id": SENSOR_ID, "valor": valor, "timestamp": timestamp}
            j = json.dumps(payload)
            r.lpush(f"sensor:{SENSOR_ID}", j)
            print('PUSHED:', j)
        except Exception as e:
            print('Error pushing to Redis:', e)
            try:
                time.sleep(2)
                r = connect()
            except Exception:
                time.sleep(5)
        time.sleep(3)

if __name__ == '__main__':
    produce_loop()
