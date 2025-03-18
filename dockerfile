# Use a Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all necessary files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
