FROM python:3.12
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt 
COPY . .
EXPOSE 5001
CMD ["python","backend.py"]
