# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

# Define the command to run your application
# CMD ["python", "app.py"]
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
