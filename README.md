
# MLOps Deployment Assignment

This project demonstrates the deployment of a machine learning model using FastAPI, Streamlit, and Docker. The goal is to create an API that serves predictions from a trained model and build a web application that interacts with the API to make predictions.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [Accessing the Application](#accessing-the-application)
- [Testing the Model](#testing-the-model)
- [Future Improvements](#future-improvements)

## Overview
The project consists of two main components:
1. **Model API**: A FastAPI service that loads a pre-trained machine learning model and provides predictions through a RESTful API.
2. **Web Application**: A Streamlit web app that allows users to input features and get predictions from the API.

## Project Structure
The project is organized as follows:

```
mlops-deployment-assignment/
├── code/
│   ├── models/                 # Contains the training script for the model
│   ├── deployment/
│   │   ├── api/                # FastAPI code and Docker setup
│   │   ├── app/                # Streamlit app code and Docker setup
│   │   └── docker-compose.yml  # Docker Compose file to run the services
├── models/                     
└── README.md                   # Project documentation   
```

## Technologies Used
- **Machine Learning**: `scikit-learn`
- **Backend API**: `FastAPI`
- **Frontend Web App**: `Streamlit`
- **Containerization**: `Docker` and `Docker Compose`

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine
- [Git](https://git-scm.com/downloads) to clone the repository

### Cloning the Repository
```bash
git clone https://github.com/yourusername/mlops-deployment-assignment.git
cd mlops-deployment-assignment
```

### Training the Model
The model has already been trained and saved to the `models` directory. If you want to retrain the model, you can do so by running:
```bash
cd code/models
python3 train_model.py
```

## Running the Project

### Step 1: Start the Docker Containers
Ensure you're in the root project directory (`mlops-deployment-assignment`) and run the following command:
```bash
docker-compose up --build
```
This will build and start both the FastAPI and Streamlit services.

### Step 2: Access the Web Application
Open your web browser and navigate to:
```
http://localhost:8501
```

### Testing the Model
1. Enter values for each feature in the Streamlit web app.
2. Click on the "Make Prediction" button to receive the predicted housing price from the model.

## Accessing the API Directly
You can test the FastAPI service directly by accessing the following endpoint:
```
http://localhost:8000/docs
```
This URL provides access to the automatically generated Swagger documentation for the API, allowing you to test the `/predict` endpoint.

## Future Improvements
- Implement authentication for the API to restrict unauthorized access.
- Deploy the model using cloud services (AWS, Azure, or GCP) for scalability.
- Add logging and monitoring to track API usage and potential errors.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
