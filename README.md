# Micro Plex Dashboard

[Dockerhub - ziadhorat/ziadhorat/micro-plex-dashboard](https://hub.docker.com/r/ziadhorat/micro-plex-dashboard)

![image](https://github.com/user-attachments/assets/52d50193-35ea-4e23-839e-b7944654605b)

## Overview
This aims to be a simple & small application that serves as a public frontend for a Plex server. 

It displays user and library statistics in a clean, intuitive interface.

Sometimes I am asked what is on my Plex server. This is my attempt at a set and forget solution.

## Features
- Display library items with totals & currently watching users.
- Simple deployment using Docker and Docker Compose.

## Environment Variables
- `PLEX_API_TOKEN`: Your Plex API token.
- `PLEX_SERVER_URL`: URL of your plex server, include http/https.
- `DASHBOARD_TITLE`: Whatever you want the page title to be.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ziadhorat/Micro-Plex-Dashboard.git
cd Micro-Plex-Dashboard
```
### 2. Create a `.env` file
Copy the .env.example to .env and fill in the necessary values

### 3. Build and run using Docker Compose
```bash
docker-compose up --build
```
### 4. Access the app
Open a web browser and navigate to `http://localhost:8501`.

## Creating a Plex API Token
[Plex Guide - Step by Step - Getting Plex Token, Nimrod](https://digiex.net/threads/plex-guide-step-by-step-getting-plex-token.15402/)

## Docker Run Command
If you prefer to run the container using `docker run`, use the following command:
```bash
docker run -d --name micro-plex-dashboard \
  -p 8501:8501 \
  -e PLEX_API_TOKEN=your_plex_api_token_here \
  -e PLEX_SERVER_URL=http://localhost:32400 \
  -e DASHBOARD_TITLE="Micro Plex Dashboard" \
  ziadhorat/micro-plex-dashboard
```

## Notes
- If you use a reverse proxy, you will require websocket support/enabled.
- Only tested with Movie/TV/Music Libraries.

## TODO
- ARM Support
- Make favicon configurable via env var (with default)
- Set Browser page title to env var (Already set for header).
- JF/Emby Support?
- Some pagination might be needed to support large libraries.
  
## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
