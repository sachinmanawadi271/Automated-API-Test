Use conftest.py for configuration
############################################################################
1. supply_url(): Add a valid base url

2. valid_user_credentials(); Add already exisiting valid user credentials

3. load_no_requests(): For load test add number of API calls

4. bearer_token(): Add already exisiting valid user credentials to receive bearer token



Installation
#######################################################################################
cd to QA-BE-Challenge-Solution
pip install pytest
pip install pytest-html-reporter


To run
######################################################################################
cd to QA-BE-Challenge-Solution
py.test -v


To generate HTML report
######################################################################################
cd to QA-BE-Challenge-Solution
py.test  --html-report=report.html