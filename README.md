# IoT Platform for Smart Buildings
## Overview
Integrated IoT platform for smart building management with modular development.

## Branching Strategy
- `master`: Protected; requires PR + CI checks.
- Feature branches: `feature/iot-sensors`, `feature/web-dashboard`.
- `feature/iot-sensors`: Sensor data collection module.
- `feature/web-dashboard`: User interface dashboard.

## Commit Guidelines
Use format: `<type>: <description>` (e.g., `feat: add sensor API`).
Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

## Milestones
- `v1.0.0`: Initial module development.
- `v2.0.0`: CI/CD integration.
Tags: `git tag -a v1.0.0 -m "Initial modules" && git push --tags`.
