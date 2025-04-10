#  Watchdog File Monitoring System

A lightweight file monitoring tool built with **Python** and containerized using **Docker**. This script continuously watches for changes in a target file or directory and performs custom actions (e.g., logging, alerts, etc.).

---

##  Features

-  Real-time file monitoring
-  Detects file changes (e.g., updates to `test.txt`)
-  Dockerized environment with Dockerfile and Compose
-  Easy to configure and deploy

---

##  Project Structure

```
watchdog-master/
│
├── watchdog_script.py       # Main Python script to monitor files
├── Dockerfile               # Build configuration for Docker image
├── docker-compose.yml       # Compose file for running the service
├── test.txt                 # Sample file for testing file changes
└── README.md                # Project documentation (this file)
```

---

##  How to Run (with Docker)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/watchdog-master.git
   cd watchdog-master
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t watchdog-app .
   ```

3. **Run with Docker Compose:**
   ```bash
   docker-compose up
   ```

The script will start monitoring `test.txt` for any changes.

---

##  Local Development (Without Docker)

> Make sure Python 3.x is installed.

1. Install dependencies (if any):
   ```bash
   pip install watchdog
   ```

2. Run the script:
   ```bash
   python watchdog_script.py
   ```



---

##  Developer

Developed by: **Niloufar Cheraghi**
