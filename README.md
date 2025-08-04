
# Fibonacci Sequence API

A RESTful API that computes the nth number in the Fibonacci sequence.

## Setup and Running Locally

1. **Prerequisites**:
   - Python 3.12+
   - pip

2. **Installation**:
```bash
git clone <repository-url>
cd fibonacci_python
pip install -r requirements.txt
```

3. **Running the API**:
```bash
uvicorn app.main:app --reload
```

4. **Accessing the API**:
   - The API will be available at `http://localhost:8000`
   - Interactive API documentation: `http://localhost:8000/docs`

## API Endpoints

- **GET /fibonacci/{n}**
- **POST /fibonacci**
- **GET /health**

## Testing

```bash
pytest
```

## Deployment Considerations

### Containerization

- Build and run:
```bash
docker build -t fibonacci-api .
docker run -p 8000:8000 fibonacci-api
```

### CI/CD Processes
Recommended setup using GitHub Actions:
- Automated testing on push/pull requests
- Build and push Docker image to registry
- Deploy to Kubernetes or cloud service
Example workflow:
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: user/fibonacci-api:latest
```

### Monitoring and Scaling

- Health check: `/health`
- Redis caching via `lru_cache`
- Rate Limiting via `fastapi-limiter`
- Add Prometheus/Grafana for metrics


## Error Handling
- Input validation for non-negative integers
- HTTP status codes for error conditions
- Graceful handling of large inputs
