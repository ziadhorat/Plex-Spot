# <img src="https://cdn-icons-png.freepik.com/256/7664/7664156.png?uid=R161963193&ga=GA1.1.651749782.1725523197&semt=ais_hybrid" alt="iCON" width="30" height="30"> PlexSpot

PlexSpot: Your Plex server's elegant public face. Showcase your media library with style and simplicity.

[![Docker Image CI](https://github.com/ziadhorat/Plex-Spot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/ziadhorat/Plex-Spot/actions/workflows/docker-image.yml) [![CodeQL](https://github.com/ziadhorat/Plex-Spot/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/ziadhorat/Plex-Spot/actions/workflows/github-code-scanning/codeql) [![Pages Build Deployment](https://github.com/ziadhorat/Plex-Spot/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ziadhorat/Plex-Spot/actions/workflows/pages/pages-build-deployment)

[Docker Hub](https://hub.docker.com/r/ziadhorat/plex-spot) | [Live Demo](https://plex-spot.labhome.co.za)

![DemoGif](https://github.com/user-attachments/assets/70c510c5-c95b-4d86-8597-0d919b554096)

## 🚀 Quick Start

```bash
docker run -d --name plex-spot \
  -p 8501:8501 \
  -e PLEX_API_TOKEN=your_token_here \
  -e PLEX_SERVER_URL=http://your_server_ip:32400 \
  ziadhorat/plex-spot
```

Access at `http://localhost:8501`

## 🌟 Why PlexSpot?

- Sleek, public-facing interface for your Plex library
- Real-time user activity and library statistics
- Effortless setup with Docker

## 🛠 Configuration

| Variable | Description | Required |
|----------|-------------|----------|
| `PLEX_API_TOKEN` | Your Plex API token | Yes |
| `PLEX_SERVER_URL` | Your Plex server URL (Use local IPv4 of plex instead of localhost) | Yes |
| `DASHBOARD_TITLE` | Custom dashboard title | No |
| `DASHBOARD_ICON` | Custom dashboard icon URL | No |
| `DEBUG` | Enable debug mode (True/False) | No |

Need help getting your Plex token? [Follow this guide](https://digiex.net/threads/plex-guide-step-by-step-getting-plex-token.15402/)

## 📊 Docker Compose

```yaml
version: '3'
services:
  plex-spot:
    image: ziadhorat/plex-spot
    ports:
      - "8501:8501"
    environment:
      - PLEX_API_TOKEN=${PLEX_API_TOKEN}
      - PLEX_SERVER_URL=${PLEX_SERVER_URL}
```

## 🤝 Contribute

Issues, features, and pull requests welcome! Let's make PlexSpot even better together.

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.
