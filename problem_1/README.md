# project-delivery problem:1

## Based on nodejs application: https://github.com/Amit-Naudiyal/iag-nodejs-app

Instructions:

+ Setup Jenkins using jenkins docker image:

	+ Clone this repository and go to problem_1 directory.
	+ Ensure you have docker-compose installed in your local system or on the machine where you are going to run Jenkins
		```
		$ docker-compose up
		```
	+ This will start a jenkins container via bridge network, on http://machine-ip:8085
	+ Once started it will give one time password like:

		```
        jenkins_1  | Jenkins initial setup is required. An admin user has been created and a password generated.
        jenkins_1  | Please use the following password to proceed to installation:
        jenkins_1  | 
        jenkins_1  | 32326792872345f7bad6a6d19afbf055
        jenkins_1  | 
        jenkins_1  | This may also be found at: /var/jenkins_home/secrets/initialAdminPassword	
		```	
	+ Access Jenkins on http://localhost:8085 (if setup on local machine) with above password. Skip other user setup.

+ Setup of pipeline

	+ This jenkins is a customized jenkins which will give an option of 'Open Blue Ocean' on left pane.
	+ Once jenkins is started, click on that button and add your SCM repository.
		Type: Github
		Generate token from developer settings and pass it here.
		Select your Application repo. _[Note: I used Amit-Naudiyal/iag-nodejs-app repository ]_
	+ Once selected, it will scan the repository and will look for Jenkinsfile for further setup process.	

+ Execution Flow:

	+ Build Pipeline will be executed and will perform following steps _[uses Jenkinsfile]_:
		+ SCM Checkout: will download the latest version from master branch.
		+ Build: will build the application based on commands provided. _npm install_
		+ Unit Tests: test the application's unit of work. _npm test_
		+ Static Code Analysis: analysis like linting. _not covered here_
		+ Code Coverage: checks the code and generates an archive to analyse later. _npm run coverage_
		+ Archival: archive/zip the code for any further deploy phase.
		+ Invoke Deploy: invokes another pipeline: deploy-pipeline
	
	+ Deploy Pipeline will be executed and will perform following steps _[uses Jenkinsfile-deploy]_:
		+ Deploy to Container: this will fetch the artifact from original pipeline and will deploy it to container.

+ End Result:

	+ Once executed, it will look like:
		![PipelineExecution](/problem_1/pic/branch_build_process.png)	
	   	![PipelineExecution](/problem_1/pic/pipeline_run2.png)