# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the app's port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
