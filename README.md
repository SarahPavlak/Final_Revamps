#Welcome to my revamps of Opim 243 Projects!

#Resources used: 
#Syncing Github: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/3e5cee08b4fa6b206ec5852b7460569f85d9be7d/notes/git.md
#Branch Operations: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/74bfcbd43e60627151ecfb9235253e4015eb0cba/exercises/ci-123.md
# Travis CI: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/74bfcbd43e60627151ecfb9235253e4015eb0cba/exercises/testing-123.md


#New Environment
# conda create -n final_revamps
# conda activate final_revamps


#Installations: 
#pip install pytest

#Setting up Travis CI:
#Log onto Travis-CI.org
#Find your repository on Github and activate it!

#Setting up Pytests
#IMPORTANT!
#Note: For some reason the executive dashboard file is having trouble reading from the dummy csv. Therefore, you MUST go into the Executive_Dashboard folder and in the app directory (my_executive_test.py) and test (my_test.py) directory, change the csv file path right under def get_top_sellers(): and def test_get_top_sellers(): respectively. It is currently set as a regular and not a relative path to my computer!