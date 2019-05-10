# Hello and welcome to my shopping cart revamp!

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

# Changes to Code - for instructor information
Further Exploration Challenges:
1.  Completed Challenge 2; writes the checkout items to a new receipt file
2.  Completed Challenge 3; Incorporates a new banana item and factors in the price per pound if bananas are selected

Project, Revisited
1.  Completed Basic Formatting Challenges: now has tests for formatting prices and timestamps
2. Completed Intermediate Challenge: Calculating Receipt Totals and Finding Products

Code Revamp:
1.  Per the grading feedback, ensured that document now has a .py extension
2.  Per the grading feedback, updated the timestamp to exclude mili-seconds for a more user-friendly experience
3.  Per the grading feedback, updated the tax rate to be consistent with NYC Sales Tax amounts
4.  Per the grading feedback, ensured that each item is properly formatted with a $ and two decimal places

# Running the script: 
1. to run this script, please navigate to the shopping_cart directory --> app directory --> and then type "python shopping.py" in your terminal 
2. for running pytests, please navigate to the shopping_cart directory and then type "pytest" in your terminal
