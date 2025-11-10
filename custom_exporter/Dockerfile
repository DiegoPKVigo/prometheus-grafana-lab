FROM python:3.8-slim
RUN pip install flask
COPY custom_exporter.py /custom_exporter.py
CMD ["python", "/custom_exporter.py"]