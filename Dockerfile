FROM tiangolo/uvicorn-gunicorn-fastapi:latest

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY ./requirements.txt ./loan_default_pipeline.joblib ./

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app .