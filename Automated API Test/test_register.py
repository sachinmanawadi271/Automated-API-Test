import pytest
import requests
import json
import random


# Post to Register a company and admin user
def test_register_valid(supply_url, name):
    url = supply_url + "/register/"
    newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    fp = open('register.json','r')
    json_input = fp.read()
    request_json = json.loads(json_input)

    #Randomly add email ID and company name
    request_json['company']['company_name'] = name
    request_json['user']['email'] = name+'@test.com'

    email_id = request_json['user']['email']
    global email_dup, company_dup 
    email_dup = email_id
    company_dup =  request_json['company']['company_name']

    #Make post request with Json
    resp = requests.post(url, data=json.dumps(request_json), headers=newHeaders)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['data']['email'] == email_id, resp.text


# Post to valid duplicate entry
def test_register_dup(supply_url):
    url = supply_url + "/register/"
    newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    fp = open('register.json','r')
    json_input = fp.read()
    request_json = json.loads(json_input)
    request_json['company']['company_name'] = company_dup
    request_json['user']['email'] = email_dup

    #Make post request with Json
    resp = requests.post(url, data=json.dumps(request_json), headers=newHeaders)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['data']['code'] == "ER_DUP_ENTRY", resp.text
    assert j['data']['errno'] == 1062, resp.text


# Post to validate missing fields
def test_register_invalid_missing_field(supply_url, name):
    url = supply_url + "/register/"
    newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    fp = open('register_invalid.json','r')
    json_input = fp.read()
    request_json = json.loads(json_input)
    request_json['user']['email'] = name+'@test.com'

    #Make post request with Json
    resp = requests.post(url, data=json.dumps(request_json), headers=newHeaders)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['data']['code'] == "ER_NO_DEFAULT_FOR_FIELD", resp.text
    assert j['data']['errno'] == 1364, resp.text


# Post request to validate company ID
def test_register_valid_company_id(supply_url, name):
    url = supply_url + "/register/"
    newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    fp = open('register_company_id.json','r')
    json_input = fp.read()
    request_json = json.loads(json_input)
    
    #Randomly add email ID and company name
    request_json['company']['company_name'] = name
    request_json['user']['email'] = name+'@test.com'

    #Random company id
    request_json['user']['company_id'] = random.randint(1000,2147483646)

    #Make post request with Json
    resp = requests.post(url, data=json.dumps(request_json), headers=newHeaders)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['data']['company_id'] == request_json['user']['company_id']


# Synchronous load test
def test_register_load(supply_url, load_no_requests, name):
    x = 0
    url = supply_url + "/register/"
    newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    fp = open('register_company_id.json','r')
    json_input = fp.read()
    request_json = json.loads(json_input)
    #Randomly add email ID and company name
    request_json['company']['company_name'] = name
    request_json['user']['email'] = name+'@test.com'

    while x!=load_no_requests:
        request_json['company']['company_name'] = name
        request_json['user']['email'] = name+str(x)+'@test.com'
        resp = requests.post(url, data=json.dumps(request_json), headers=newHeaders)
        j = json.loads(resp.text)
        assert resp.status_code == 200, resp.text
        assert j['data']['email'] == request_json['user']['email'], resp.text
        x = x+1