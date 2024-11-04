# Advanced Web Technologies

This repository contains lab work and submissions for the **Advanced Web Technologies** course project.

## Prerequisites

Before running the project, make sure you have the following installed on your computer:

- **Docker**: Ensure you have Docker installed and running. You can download it from [Docker's official website](https://www.docker.com/get-started).

- **Git**: To clone the repository, make sure you have Git installed. You can download it from [Git's official website](https://git-scm.com/downloads).

## Cloning the Repository

To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/Blade-iii/Advanced-Web-Technologies.git

## Docker Commands

To build and run your Docker container for the Flask application, use the following commands:

```bash
# Navigate to the project directory
cd Advanced-Web-Technologies/Coursework

# Build the Docker image
docker build -t dockerfile .

# Run the Docker container
docker run -p 5000:5000 dockerfile
