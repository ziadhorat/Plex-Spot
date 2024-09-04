# Micro Plex Dashboard

## Overview
This aims to be a simple & small application that serves as a public frontend for a Plex server. 

It displays user and library statistics in a clean, intuitive interface.

## Features
- Display currently watching users, and library items with totals.
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

## TODO
- ARM Support
- Make favicon configurable
- Make page title in status bar to same as title.
  
## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
