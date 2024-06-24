# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable (replace YOUR_ACCESS_TOKEN with the actual token)
ARG SECLYTICS_ACCESS_TOKEN
ENV SECLYTICS_ACCESS_TOKEN=${SECLYTICS_ACCESS_TOKEN}

# Download the database
CMD python -m seclytics.scripts.download_db --access_token $SECLYTICS_ACCESS_TOKEN --name predicted-ips.bloom,malicious-ips.bloom,ip-threat-intel.bloom --data-dir /tmp

# Run the IP filter script with a test IP address
CMD echo '51.255.139.200' | python -m seclytics.scripts.ip_filter --suspicious --malicious --predicted