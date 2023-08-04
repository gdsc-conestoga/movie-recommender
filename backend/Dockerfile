FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN python3 ml-builder.py
EXPOSE 5000
CMD ["python", "api.py"]
