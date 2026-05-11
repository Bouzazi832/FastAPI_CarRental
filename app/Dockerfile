FROM python:3.9-slim

WORKDIR /code

# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code from the current folder (app/) to the container (/code)
COPY . .

# Run uvicorn. 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]