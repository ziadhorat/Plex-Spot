# Plex Streamlit Dashboard

## Overview
This is a simple, yet powerful, Streamlit application that serves as a public frontend for a Plex server. It displays user and library statistics in a clean, intuitive interface.

## Features
- Display user statistics such as total users, currently watching users, and users active in the last week.
- Display detailed library statistics including movies, TV shows, and music.
- Configurable caching to optimize performance.
- Simple deployment using Docker and Docker Compose.

## Environment Variables
- `PLEX_API_TOKEN`: Your Plex API token.
- `DISPLAY_USER_STATS`: Set to `True` to display user statistics.
- `DISPLAY_LIBRARY_STATS`: Set to `True` to display library statistics.
- `CACHE_DURATION`: Time (in seconds) to cache API responses. Defaults to 300 seconds.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/plex-streamlit-app.git
cd plex-streamlit-app
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
docker run -d --name plex-streamlit-app \
  -p 8501:8501 \
  -e PLEX_API_TOKEN=your_plex_api_token_here \
  -e DISPLAY_USER_STATS=True \
  -e DISPLAY_LIBRARY_STATS=True \
  -e CACHE_DURATION=300 \
  your-username/plex-streamlit-app
```
## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
