# Distributed System Failure Injection Simulator
docker-compose up --build
curl http://localhost:5000/request

## Overview
This project simulates a distributed microservices system and injects controlled failures to study resilience, recovery behavior, and fault propagation.

## Architecture
- Service A: API Gateway
- Service B: Core Processing
- Service C: Logging
- Failure Injector: Injects faults

## Failure Types Implemented
- Service crash
- Latency injection
- Network partition (simulated)

## Experiments
See `/experiments` folder for detailed failure studies.

## Tech Stack
- Python
- Flask
- Docker & Docker Compose

## Learnings
- Distributed systems rarely fail cleanly
- Timeouts and retries are critical
- Partial failure handling improves resilience

## Future Work
- Automated chaos scheduling
- Metrics dashboard
- Real network partition using tc
