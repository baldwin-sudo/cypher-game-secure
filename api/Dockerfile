# Use the official Miniconda image from the Docker Hub
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the environment.yml file into the container
COPY environment.yml /app/

# Create the Conda environment
RUN conda env create -f environment.yml

# Set environment variables for Conda
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 3000

# Define environment variable
ENV FLASK_APP=app.py

# Activate the Conda environment and run the application
CMD ["python", "app.py"]
