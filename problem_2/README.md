# project-delivery problem:2

## Implemented by script: iag-project2.py

Instructions:

+ AWS Services involved:

	+ S3 : Object storage where pdf will be uploaded
	+ Lambda: Serverless compute where this script will be executed.
	+ IAM : Permissions by Lambda function to read and do operation on S3 bucket and write logs to Cloudwatch logs.

+ Instructions to follow:

	+ Create an S3 bucket with any unique name and create one folder named: final-file inside it. Keep permissions defaut (no public).	
	+ Add the script to Lambda function.
	+ Replace the string 'iag-project2' with your S3 bucket name created in 1st step.
	+ Ensure to use a Lambda role that have full permissions on S3 and Cloudwatch. These can be restricted in case required.
	+ Create an Event on this S3 bucket for 'Put' operation which will invoke a 'Lambda function'. Choose above Lambda that was created.

+ Execution Flow:

	+ User uploads a file with pdf extension on this S3 bucket.
	+ S3 event will be invoked due to this put operation which will trigger Lambda function.
	+ Lambda will execute the function to connect to S3 bucket and find the object/file. 
		+ Lambda will print the Filename. 
		+ Then it will check if the file has pdf extension.
		+ If yes, it will rename the file by appending a latest timestamp.
		+ Then it is moved to a folder named: final-file.
