# Hello and welcome to my robo advisor revamp!

Resources used: 
1. Syncing Github: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/3e5cee08b4fa6b206ec5852b7460569f85d9be7d/notes/git.md
2. Branch Operations: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/74bfcbd43e60627151ecfb9235253e4015eb0cba/exercises/ci-123.md
3. Travis CI: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/74bfcbd43e60627151ecfb9235253e4015eb0cba/exercises/testing-123.md

# Code Setup Instructions
New Environment
1. conda create -n final_revamps
2. conda activate final_revamps

Installations: 
1. pip install pytest
2. pip install -r requirements.txt

Setting up Travis CI:
1. Log onto Travis-CI.org
2. Find your repository on Github and activate it!

Security requirements:
1. Within the app directory, create a .env file
2. Navigate to https://www.alphavantage.co/ and request an API Key
3. Within your .env file, type "MY_API_KEY='your_api_key_goes_here' This will create an environment variable for you which will ensure that your key remains secure.
3. Within the app directory, create a ".gitignore" file. Within this file, type ".env"

# Changes to Code - for instructor information
Further Exploration Challenges:
1.  Per the travis file, it should run automated tests

Project, Revisited
1.  Completed basic challenges: formatting prices and compiling request URLs
2.  Completed intermediate challenges: tests to ensure that a csv file is written and that it has the proper headers
3. Completed intermediate challenges: api issuing and api requests

Code Revamp:
1.  Per the grading feedback, changed the csv file path; the csv data is now inside the app directory so it should not have the same file not found error
2. Per the grading feedback, erased lines to ensure that request was not being submitted more than once 
3. Per the grading feedback, redid the stock recommendation to make more sense and be more clear

# Running the script: 
1. to run this script, please navigate to the robo_advisor directory --> app directory --> and then type "python my_robo.py" in your terminal 
2. IMPORTANT: For running pytests, please navigate to the robo_advisor directory --> app directory --> my_robo_test.py document and, on line 55 where it says exists = os.filepath, make sure that you change my hardcoded path to the one specific to your computer. The relative file path will not work. 
3. For running pytests please navigate to the robo_advisor (note: not the app directory! If you are in app make sure you cd ..) directory and then type "pytest" in your terminal

