# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt (you can create this by running pip freeze > requirements.txt)
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the app's port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
