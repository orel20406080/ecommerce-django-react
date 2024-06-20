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
#print('Hello %s from Jenkins %s' % (user['fullName'], version))

print(f"Hello {user['fullName']} from Jenkins {version}")

## Jobs 

# Create empty job
# server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

# copy job1 to job2

# create a job and put it in a xml file
# job2_xml = open("job2.xml", mode="r", encoding="utf-8").read()
# server.create_job("job2", job2_xml)

# View jobs
jobs = server.get_jobs()
print(jobs)

# Get all jobs from the specific view
# jobs = server.get_jobs(view_name='View Name')
# print jobs

# get the job config
# job1 = server.get_job_config('job1')
# print(job1)

# disable a job 
# server.disable_job('job1')

# enable disabled job
# server.enable_job('job1')

# delete a job
# server.delete_job('job1')
# server.delete_job('job2')

#job_name = jobs[0]['name']
#server.build_job(job_name)
#job_number = server.get_job_info(job_name)['lastCompletedBuild']['number']

#print(job_number)
#print(f'Job {job_name} has been started!')

#print(server.get_build_console_output(job_name, job_number))

## Builds

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
# server.build_job('job1', {'param1': 'test value 1', 'param2': 'test value 2'})
# last_build_number = server.get_job_info('job1')['lastCompletedBuild']['number']
# build_info = server.get_build_info('job1', last_build_number)
# print(build_info)

# Start a build
# server.build_job('job1')

# Get build number
# last_build_number = server.get_job_info('job1')['lastCompletedBuild']['number']
# print('Build Number', last_build_number)

# Stop build
# server.stop_build('job1', last_build_number)

# Delete build
# server.delete_build('job1', last_build_number)

## Views

# Create a view
# view_config = open("jobs_view.xml", mode="r", encoding="utf-8").read()
# server.create_view('Job List', view_config)

# Get view list
# views = server.get_views()
# print(views)

# Update a view
# updated_view_config = open("jobs_view_updated.xml", mode="r", encoding="utf-8").read()
# server.reconfig_view("Job List", updated_view_config)

# Delete a view
# server.delete_view("Job List")
