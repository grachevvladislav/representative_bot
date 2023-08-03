FROM python:3.11-slim
WORKDIR /bot
COPY bot/ .
CMD ["ls"]
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python", "src/main.py" ]