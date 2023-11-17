# Project: Setting up Application Server for Airbnb Clone

This project aims to integrate an application server into an existing web infrastructure to serve dynamic content for an Airbnb clone project.

## Objective

- Set up an application server to serve dynamic content.
- Integrate the application server with Nginx for seamless operation.
- Ensure proper functionality and compliance with specified requirements.

## Concepts Covered

- Web Server
- Server
- Web stack debugging

## Resources

- [Application server vs web server](link_here)
- [How to Serve a Flask Application with Gunicorn and Nginx](link_here)
- [Running Gunicorn](link_here)
- [Upstart documentation](link_here)

## Requirements

### General

- All Python-related tasks must use python3.
- Config files should be adequately commented.
- Bash scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1).
- Server configuration must be done on Ubuntu 16.04 LTS.

### Bash Scripts

- Scripts should end with a new line.
- All scripts must be executable.
- The first line of Bash scripts should be `#!/usr/bin/env bash`.
- The second line should explain the script's purpose in a comment.

### Server Information

| Name           | Username | IP             | State   |
|----------------|----------|----------------|---------|
| 277113-web-01  | ubuntu   | 54.87.234.24   | running |
| 277113-web-02  | ubuntu   | 18.235.243.195 | running |
| 277113-lb-01   | ubuntu   | 35.153.93.22   | running |
