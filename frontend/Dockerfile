FROM python:3.17
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]