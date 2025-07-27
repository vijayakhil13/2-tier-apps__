FROM python:3.17
WORKDIR ./app
COPY requirement.txt ./
RUN pip install -r requirement.txt
COPY . ./app
EXPOSE 90
CMD["python", pip"]