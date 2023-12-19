FROM python:3.10-alpine

# Install flask library
RUN pip install flask

WORKDIR /app
COPY . .

CMD ["python", "app.py" ]

EXPOSE 80