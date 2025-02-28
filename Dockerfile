# Use the specified image from GitHub Container Registry
FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN uv install

# Make port 80 available to the world outside this container
EXPOSE 7777

# Run server.py when the container launches
CMD ["uv", "run", "server.py"]