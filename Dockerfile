# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Define environment variables to disable CUDA
ENV CUDA_VISIBLE_DEVICES=-1
ENV TF_CPP_MIN_LOG_LEVEL=2

# Install necessary build tools for celeb-detector
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    cmake \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app /app

# Expose port 5080 for the Flask app
EXPOSE 80

# Run Gunicorn when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

