# Use the Python image as the base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the token.txt file into the container's working directory
COPY token.txt .

# Copy all the scripts into the container's working directory
COPY . .

# Install the required Python packages
RUN pip install discord

# Run the Main.py script when the container starts
CMD ["python", "main.py"]
