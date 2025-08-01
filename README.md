# 🚀 Docker Streamlit App

A modern, interactive Streamlit application running in a Docker container with a beautiful UI and multiple features.

## ✨ Features

- 📊 **Interactive Dashboard** - Real-time metrics and charts
- 📈 **Data Visualization** - Upload CSV files and create interactive plots
- 🎮 **Interactive Demo** - Various Streamlit widgets and controls
- 📁 **File Upload** - Upload and analyze CSV data
- 🎨 **Modern UI** - Beautiful, responsive design
- 🔄 **Docker Ready** - Fully containerized application

## 🛠️ Technology Stack

- **Streamlit** - Web app framework
- **Docker** - Containerization
- **Python 3.11** - Backend language
- **Plotly** - Interactive charts
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Clone or download the project files**
2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```
3. **Open your browser:** `http://localhost:8501`

### Option 2: Using Docker Commands

1. **Build the Docker image:**
   ```bash
   docker build -t streamlit-app .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8501:8501 streamlit-app
   ```

3. **Open your browser:** `http://localhost:8501`

### Option 3: Development Mode

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Streamlit locally:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📁 Project Structure

```
pjcstreamlit/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Docker ignore file
└── README.md            # This file
```

## 🎯 App Pages

### Dashboard
- Real-time metrics display
- Sample time series chart
- Responsive layout with multiple columns

### Data Visualization
- CSV file upload functionality
- Interactive data preview
- Dynamic chart generation
- Statistical analysis

### Interactive Demo
- Various Streamlit widgets
- Form controls and inputs
- Real-time interaction examples

### About
- Project information
- Technology stack details
- Setup instructions

## 🔧 Configuration

### Environment Variables

The app uses the following environment variables:

- `PYTHONUNBUFFERED=1` - Ensures Python output is not buffered
- `PYTHONDONTWRITEBYTECODE=1` - Prevents Python from writing bytecode files

### Port Configuration

The app runs on port `8501` by default. You can change this by:

1. **Docker Compose:** Modify the ports section in `docker-compose.yml`
2. **Docker Run:** Use `-p <host-port>:8501` when running the container

## 🐳 Docker Commands

### Build and Run
```bash
# Build image
docker build -t streamlit-app .

# Run container
docker run -p 8501:8501 streamlit-app

# Run in background
docker run -d -p 8501:8501 --name my-streamlit-app streamlit-app
```

### Docker Compose
```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# Rebuild and start
docker-compose up --build
```

### Container Management
```bash
# List running containers
docker ps

# View logs
docker logs <container-name>

# Stop container
docker stop <container-name>

# Remove container
docker rm <container-name>
```

## 📊 Data Upload

The app supports CSV file uploads for data visualization. Uploaded files are processed in memory and not stored permanently.

### Supported Formats
- CSV files with headers
- Numeric and text columns
- Files up to 200MB (Streamlit default limit)

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Check what's using port 8501
   lsof -i :8501
   
   # Use a different port
   docker run -p 8502:8501 streamlit-app
   ```

2. **Docker build fails:**
   ```bash
   # Clean Docker cache
   docker system prune -a
   
   # Rebuild without cache
   docker build --no-cache -t streamlit-app .
   ```

3. **App not loading:**
   ```bash
   # Check container logs
   docker logs <container-name>
   
   # Check container health
   docker inspect <container-name>
   ```

### Performance Tips

1. **For development:** Use volume mounting for live code changes
2. **For production:** Build optimized images without development dependencies
3. **For large datasets:** Consider using external databases or data stores

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [Plotly](https://plotly.com/) for interactive visualizations
- [Docker](https://www.docker.com/) for containerization

---

**Happy coding! 🚀** 