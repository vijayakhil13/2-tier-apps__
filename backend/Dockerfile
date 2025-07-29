FROM python:3.12
WORKDIR /app
COPY reqirements.txt .
RUN pip install -r reqirements.txt 
COPY . .
EXPOSE 5001
CMD ["python","backend.py"]
