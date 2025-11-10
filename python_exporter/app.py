from prometheus_client import start_http_server, Summary, Counter
import random
import time

# Create metrics to track processing time and request counts.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@REQUEST_TIME.time()
def process_request(t):
  time.sleep(t)
  REQUEST_COUNT.inc()

if __name__ == '__main__':
  # Expose metrics at port 8000
  start_http_server(8000)
  while True:
    process_request(random.random())
