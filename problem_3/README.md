# project-delivery problem:2

## Implemented by script: iag-project3.py

#### Instructions:

+ Installation:
	+ Install/Place this script on any Linux based instance.
	+ Ensure you have Python 3.8 installed.
	+ Install dependencies: 
```
		pip3.8 install flask
		pip3.8 install requests
		pip3.8 install request
```

+ Execution & Access:
	+ Run :
		$ python 3.8 iag-project3.py

		 * Serving Flask app "iag-project3-new" (lazy loading)
		 * Environment: production
		   WARNING: This is a development server. Do not use it in a production deployment.
		   Use a production WSGI server instead.
		 * Debug mode: off
		 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)

	+ Access it on http://localhost:5001

+ Flow:
	+ It contains 2 boxes : 
		+ Add Textbox: To add a textbox to insert the URL to monitor.			
		+ Remove Texbox: Remove a textbox where monitoring is no longer needed.
	+ While entering URL, use http or https. It will fail without them.
		
	_Note: Currently it only monitors that responds with only 200 status codes._
	
	+ Once entered, click on Select
	+ It will give the status of the website, if it is up or down.

	_Note: Currently it is manual, but can be automated by putting a while loop for 30 seconds._
