import pytest
import requests
import json


# Get companies for an authenticated user
def test_companies_valid(supply_url, bearer_token):
    url = supply_url + "/companies/"
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.get(url, headers=header)
    assert resp.status_code == 200, resp.text


# Get companies for an unauthenticated user
def test_companies_invalid(supply_url):
    bearer_token ="sadadadsdafodfodnf"
    url = supply_url + "/companies/"
    header = {'Authorization': 'Bearer ' + bearer_token}
    resp = requests.get(url, headers=header)
    assert resp.status_code == 401, resp.text