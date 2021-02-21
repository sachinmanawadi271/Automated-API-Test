import pytest
import requests
import json
import random
import string

@pytest.fixture
def supply_url():
	return "http://localhost:3333/api/v1"

@pytest.fixture
def valid_user_credentials():
	return {'email':'test@test.com','password':'Tst123!'}

@pytest.fixture
def name():
	name = ''.join(random.choice(string.ascii_letters) for i in range(7))
	return name

@pytest.fixture
def load_no_requests():
	return 5

@pytest.fixture
def bearer_token(supply_url,valid_user_credentials):
	url = supply_url + "/login/"
	data = valid_user_credentials#{'email':'test@test.com','password':'Tst123!'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	if resp.status_code == 200:
		return j['data']['token']['token']
	else:
		return ""