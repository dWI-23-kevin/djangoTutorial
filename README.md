# Django Tutorial


To build the Docker image of the application, run the following command in the root of the project:
```bash
docker build -t djangotutorial:latest .

docker run -p 8000:8000 djangotutorial:latest
