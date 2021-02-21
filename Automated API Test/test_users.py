import pytest
import requests
import json
import logging

# Create users with valid auth key
def test_users_create_valid(supply_url, bearer_token, name):
    url = supply_url + "/users/create/"
    data = {'email':name+'@test.com','password':'Tst1234!'}
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.post(url, data=data, headers=header)
    assert resp.status_code == 200, resp.text


#Create users with invalid auth key
def test_users_create_invalid(supply_url):
    bearer_token ="sadadadsdafodfodnf"
    url = supply_url + "/users/create/"
    data = {'email':'test1@test.com','password':'Tst1234!'}
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.post(url, data=data, headers=header)
    assert resp.status_code == 401, resp.text


# Get user list with valid auth keys
def test_users_valid(supply_url, bearer_token):
    url = supply_url + "/users/"
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.get(url, headers=header)
    assert resp.status_code == 200, resp.text


# Get user list with invalid auth keys
def test_users_invalid(supply_url):
    bearer_token ="sadadadsdafodfodnf"
    url = supply_url + "/users/"
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.get(url, headers=header)
    assert resp.status_code == 401, resp.text


# Get user list with valid auth keys with id parameter
def test_users_id_valid(supply_url, bearer_token):
    url = supply_url + "/users/"
    data = {'id':1}
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.get(url, data=data, headers=header)
    assert resp.status_code == 200, resp.text

# Get user list with invalid auth keys with id parameter
def test_users_id_invalid(supply_url):
    bearer_token ="sadadadsdafodfodnf"
    url = supply_url + "/users/"
    data = {'id':1}
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.get(url, data=data, headers=header)
    assert resp.status_code == 401, resp.text
