from flask import Flask, Response

app = Flask(__name__)

@app.route('/custom-metrics')
def custom_metrics():
  # Custom metrics in Prometheus exposition format
  metrics_data = """
# HELP my_custom_metric A custom metric example.
# TYPE my_custom_metric counter
my_custom_metric 42
"""
  return Response(metrics_data, mimetype='text/plain')

if __name__ == '__main__':
  # Listen on port 8001
  app.run(host='0.0.0.0', port=8001)
