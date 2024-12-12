FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the application
CMD ["python", "app.py"]
