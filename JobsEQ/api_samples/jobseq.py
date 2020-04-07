"""JobsEQ utilities for retrieving OAuth token and running an analytic"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen, quote
from urllib.error import URLError, HTTPError
import getpass
import json

# API KEY = '5518A0D1-62E9-4CCA-9FB0-527E27A0A3BB'

JOBSEQ_URL = 'http://jobseq.eqsuite.com'


def get_token(username=None, password=None):
    """Get auth token that is valid for 1 day from JobsEQ
    via an HTTP API call using a username and password"""

    # Create the request params
    jobseq_username = username if username is not None else input(
        'Enter your JobsEQ username: ')
    jobseq_password = password if password is not None else getpass.getpass(
        'Enter your JobsEQ password: ')
    jobseq_token_endpoint = '{0}/token'.format(JOBSEQ_URL)
    jobseq_token_param_string = 'grant_type=password&username={0}&password={1}'.format(
        jobseq_username, jobseq_password)
    jobseq_token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    # Create the request to be sent
    req = Request(jobseq_token_endpoint, jobseq_token_param_string.encode('utf-8'), jobseq_token_headers)

    # Try to send the request and return the token
    try:
        with urlopen(req) as res:
            # return the access token from the oauth response
            return json.loads(res.read().decode('utf-8'))['access_token']
    except HTTPError as error:
        print('The server couldn\'t fulfill the request. Error code: {0}'.format(error.code))
        print('Error response body: {0}'.format(error.read()))
    except URLError as error:
        print('We failed to reach a server.')
        print('Reason: ', error.reason)

    # exit if an error has occurred
    exit()


def run_analytic(auth_token, analytic_id, analytic_params):
    """Call the JobsEQ API run_analytic endpoint with the provided
    params and return the analytic response as a Python dictionary"""

    # Create the request params to call the runanalytic endpoint with the provided analytic id & params
    request_url = '{0}/api/external/runanalytic?id={1}'.format(JOBSEQ_URL, analytic_id)
    request_headers = {
        "Authorization": 'Bearer {}'.format(auth_token),
        "Content-Type": "application/json"
    }
    request_data = json.dumps(analytic_params).encode('utf8')

    # Create the actual request
    req = Request(request_url, request_data, request_headers)

    # Try to send the request and return the response
    try:
        with urlopen(req) as res:
            # return the data from the analytic request
            return json.loads(res.read().decode('utf-8'))
    except HTTPError as error:
        print('The server couldn\'t fulfill the request. Error code: {0}'.format(error.code))
        print('Error response body: {0}'.format(error.read()))
    except URLError as error:
        print('We failed to reach a server.')
        print('Reason: ', error.reason)

    # exit if an error has occurred
    exit()
