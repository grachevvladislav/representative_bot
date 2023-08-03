FROM python:3.11-slim
COPY bot/ .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python", "src/main.py" ]