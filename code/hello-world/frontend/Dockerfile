FROM python:3.10-alpine

# Install flask library
RUN pip install flask requests

WORKDIR /frontend
COPY frontend.py .


CMD ["python", "frontend.py" ]

EXPOSE 80