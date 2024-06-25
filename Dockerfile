# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir watchdog

# Define environment variable
ENV FILE_TO_WATCH=/app/test.txt

# Add entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Run entrypoint script when the container launches
ENTRYPOINT ["/app/entrypoint.sh"]
