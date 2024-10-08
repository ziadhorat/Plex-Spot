# <img src="https://cdn-icons-png.freepik.com/256/7664/7664156.png?uid=R161963193&ga=GA1.1.651749782.1725523197&semt=ais_hybrid" alt="iCON" width="30" height="30"> PlexSpot

This aims to be a simple & small application that serves as a public frontend for a Plex server. 

It displays user and library statistics in a clean, intuitive interface.

Sometimes I am asked what is on my Plex server. This is my attempt at a set and forget solution.

Links: [Dockerhub - ziadhorat/plex-spot](https://hub.docker.com/r/ziadhorat/plex-spot) | [Demo](https://plex-spot.labhome.co.za)

![DemoGif](https://github.com/user-attachments/assets/f4291068-7d92-4217-8720-66abdfae26ba)

## 🌟 Features
- Display all library items with totals & currently watching users (No auth).
- Simple deployment using Docker and Docker Compose.

## ⚙️ Environment Variables
- `PLEX_API_TOKEN`: Your Plex API token. **[Required]**
- `PLEX_SERVER_URL`: Points to your plex server, localhost/127.0.0.1 may not work use IPv4 address instead. **[Required]**
- `DASHBOARD_TITLE`: Page & Site title can be configured here. **[Optional]**
- `DASHBOARD_ICON`: Page & Site icon can be configured here. **[Optional]**
- `DEBUG`: True/False, Enables debug info. **[Optional]**

### Creating a Plex API Token
[Plex Guide - Step by Step - Getting Plex Token, Nimrod](https://digiex.net/threads/plex-guide-step-by-step-getting-plex-token.15402/)

## 🚀 Docker Run Command
If you prefer to run the container using `docker run`, use the following command:
```bash
docker run -d --name plex-spot \
  -p 8501:8501 \
  -e PLEX_API_TOKEN=your_plex_api_token_here \
  -e PLEX_SERVER_URL=http://localhost:32400 \
  -e DEBUG=False \
  ziadhorat/plex-spot
```
Open a web browser and navigate to `http://container-ip:8501`.

## 📊 Deploy with docker compose

Create a `.env` file:
```
# Plex Server URL
PLEX_SERVER_URL=http://localhost:32400
# Plex API Token - See README.md
PLEX_API_TOKEN=your_plex_api_token
# Dashboard settings
DASHBOARD_TITLE="PlexSpot"
DASHBOARD_ICON="https://cdn-icons-png.freepik.com/256/7664/7664156.png"

# Debug can be enabled below with True
DEBUG=False
```

Create a `docker-compose.yml`:
```yaml
version: '3'
services:
  plex-spot:
    container_name: plex-spot
    image: ziadhorat/plex-spot
    ports:
      - "8501:8501"
    environment:
      - PLEX_API_TOKEN=${PLEX_API_TOKEN}
      - PLEX_SERVER_URL=${PLEX_SERVER_URL}
      - DASHBOARD_TITLE=${DASHBOARD_TITLE}
      - DASHBOARD_ICON=${DASHBOARD_ICON}
      - DEBUG=${DEBUG}
```
Run `docker compose up -d`.

Open a web browser and navigate to `http://container-ip:8501`.

## 📋 Notes
- localhost/127.0.0.1 may not work use IPv4 address instead
- Tested with Movie/TV/Music Libraries (Supports 1 server only).

## 📌 Local development (docker compose)

### 1. Clone the repository
```bash
git clone https://github.com/ziadhorat/Plex-Spot.git
cd Plex-Spot/development
```
### 2. Create a `.env` file
Copy the `.env.example` to `.env` and fill in the necessary values

### 3. Build and run using Docker Compose
```bash
docker-compose up --build
```
### 4. Access the app
Open a web browser and navigate to `http://localhost:8501`.

## 📝 TODO
- Dark mode toggle issues
- Rename to media-library so Plex doesn't sue me.
- Display poster or artist covers, with IMDb links if available.
- Add support for multiple Plex servers (e.g., PLEX1, PLEX2).
- Extend support to additional media servers like Emby or Jellyfin.
- Consider querying Tautulli instead of Plex for better data access.
- Fix importing of OS everywhere and rather handle debug true/false status in the logger.
- Debug logs need to be cleaned up.
  
## ✨ Contributing
Feel free to submit issues, feature or pull requests. 
All contributions are welcome!

## 📜  License
This project is licensed under the MIT License. See the LICENSE file for details.
