#  hi-automation
Hosting-Israel
# #  Project setup
```
comands here
```




# # pytest
# run all test cases
py.test 

# run Home page test (test_homepage)
pytest -k homepage -v

# fixtures
# function(once per session), session(package), module(once per module), class(once per class)

# run Home page test with markers (@pytest.mark.home)
pytest -m home

# parallel mode (pip install pytest-xdist)
pytest test_google_search -n 3

# add html reports (pip install pytest-html)
pytest test_google_search.py -v -s --html=google_test_report.html