# Stage 1: Build dependencies in a temporary image
FROM python:3.9-slim AS builder

WORKDIR /app

# Install pip-tools to compile a minimal requirements file
RUN pip install --no-cache-dir pip-tools

# Copy only the necessary files for the app
COPY requirements.in .

# Compile a minimal requirements.txt
RUN pip-compile --output-file=requirements.txt requirements.in

# Stage 2: Final image with a minimal footprint
FROM python:3.9-slim AS final

WORKDIR /app

# Install dependencies using the minimal requirements.txt
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files to the final image
COPY app/ app/
COPY main.py .

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true

# Expose port 8501
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]

