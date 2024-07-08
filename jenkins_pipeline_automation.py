#!/usr/bin/env python3

import jenkins
import json
import os

host = "http://localhost:8080"
username = "orel"
password = "1142e1eac9b495bf374478a1dc2fd16c20"

server = jenkins.Jenkins(host, username, password)

# Test the api communication
user = server.get_whoami()
version = server.get_version()
print(f"Hello {user['fullName']} from Jenkins {version}")

# Jobs 
jobs = server.get_jobs()
print(jobs)

# Start a build
job_name = 'ci-cd ecommerce'  # Replace with your job name
server.build_job(job_name)
print(f'Build for job {job_name} has been started!')