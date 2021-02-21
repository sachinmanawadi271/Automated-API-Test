import pytest
import requests
import json


# Test to verify login endpoint with valid username and password
def test_login_valid(supply_url, valid_user_credentials):
	url = supply_url + "/login/"
	data = valid_user_credentials
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['data']['user']['email'] == valid_user_credentials['email'], resp.reason

# Test to verify login endpint with valid username and invalid password
def test_login_no_password(supply_url):
	url = supply_url + "/login/" 
	data = {'email':'test@test.com'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.reason
	assert j['message'] == "Invalid username/password. Please try again!", resp.reason

# Test to verify login endpint with invalid username and password
def test_login_no_email(supply_url):
	url = supply_url + "/login/" 
	data = {'password':'Tst123!'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['message'] == "Invalid username/password. Please try again!", resp.reason