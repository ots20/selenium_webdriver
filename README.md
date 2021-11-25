# selenium_webdriver
Topic Classic framework - In this branch 'classic_framework' you will find the files: 
  test/selenium_webdriver_tests.py - TC level, with the class containing the tests and setUpClass & tearDownClass 
  pages/ 
    .py files with the interacted elements of every page or component the TC use, the locators are on those files as well 
    base_page.py - contains the methods which control the browser and initializes the WebDriver 

-------------------------

SETUP 
1.- open a terminal 
2.- run git clone git@github.com:https://github.com/ots20/selenium_webdriver.git to clone the repository 
3.- run cd bootcamp_selenium_classic_framework to move to local repository folder 
4.- run pipenv install -d to set up all the dependencies from Pipfile.lock 
5.- run pipenv shell in order to usee pipenv dependencies from the terminal 

-------------------------

EXECUTION 
1.- open a terminal 
2.- run python3 -m unittest test/selenium_webdriver_tests.py 