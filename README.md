# Project Delivery
Comprise of 3 different problems

# Summary of what is being delivered

+ problem1:
	+ An end to end Jenkins pipeline that uses a public jenkins docker image.
		+ This jenkins container is started using docker-compose command.
	+ Pulls code from SCM, builds it, archive it and invoke another pipeline for deploy.
	+ Next pipeline pulls the artifact and deploys it to a container.
	+ Check individual project for more details.

+ problem2:
	+ Whenever a user uploads a pdf file to an S3 bucket, it will invoke a Lambda function.
	+ Lambda function will scan the file and verify if it has 'pdf' extension.
	+ If yes, it will append a timestamp and move it to a different folder.
	+ Multiple AWS services in use.
	+ Check individual project for more details.

+ problem3:
	+ A python code that gives you a web console to input your website to monitor.
	+ Expects URL starting from http/https.
	+ Check individual project for more details.