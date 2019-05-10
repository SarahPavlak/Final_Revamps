# Hello and welcome to my executive dashboard revamp!


Resources used: 
1. Syncing Github: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/3e5cee08b4fa6b206ec5852b7460569f85d9be7d/notes/git.md
2. Branch Operations: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/74bfcbd43e60627151ecfb9235253e4015eb0cba/exercises/ci-123.md
3. Travis CI: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/74bfcbd43e60627151ecfb9235253e4015eb0cba/exercises/testing-123.md

# Running the code!

New Environment (In your terminal type)
1. conda create -n final_revamps
2. conda activate final_revamps


Installations: 
1. pip install pytest
2. pip install -r requirements.txt

Setting up Travis CI:
1. Log onto Travis-CI.org
2. Find your repository on Github and activate it!

Setting up Pytests
1. IMPORTANT! For some reason the executive dashboard file is having trouble reading from the dummy csv. Therefore, you MUST go into the Executive_Dashboard folder and in the app directory (my_executive_test.py) and test (my_test.py) directory, change the csv file path right under def get_top_sellers(): and def test_get_top_sellers(): respectively. It is currently set specifically for my computer so you have to copy the file path to your own. 

Running this file:
1. Enter the Executive_Dashboard sub repo --> enter the app sup repo --> type "python executive.py" in your terminal
2. To run pytests, get out of the app repo (cd ..) and ensure your pwd is the broader Executive_Dashboard. Type "pytest" in your terminal 

# For instructor purposes:

Further Exploration Challenges:
1. Completed Challenge 1: Validate CSV headers
2. Completed Challenge 2: Terminal Outputs show what it would be like with normalized data

Project, Revisited
1. Completed Basic Formatting Challenges: now has tests for formatting prices 
2. Completed Intermediate Challenge: Now has test for a dummy csv top seller

Code Revamp:
1. Per the grading feedback, transformed hardcoded structure into dynamic structure!
2. Per the grading feedback, ensured that terminal outputs are properly formatted with dollar signs
3. Added a new chart; a pie chart with top 5 sellers
4. Unable to accomplish: still could not get the graphs to format with proper $ but did ensure that they had two decimals. The $ was not compatible with the format of the axis. 
