"""
Imported by doppler_env.pth Automatically inject Doppler secrets as environment variables when spawning a Python process if the `DOPPLER_ENV` environment variable is set
"""
from base64 import b64encode
import io
import os
import subprocess
import sys
import urllib.request
import urllib.error

from dotenv import load_dotenv

def print_debug_info():
    print(f'Python path: {sys.executable}')
    print(f'Working directory: {os.getcwd()}')

def fetch_cli():
    DOPPLER_ENV_COMMAND = os.environ.get(
        'DOPPLER_ENV_COMMAND', 'doppler secrets download --no-file --format env'
    )

    # If non-zero exit code, catch Python exception so only output is stderr from Doppler CLI
    try:
        return subprocess.check_output(DOPPLER_ENV_COMMAND.split()).decode('utf-8')
    except subprocess.CalledProcessError as err:
        print_debug_info()


def fetch_api(doppler_token, format):    
    auth_header = b'Basic %s' % b64encode(f'{doppler_token}:'.encode('ascii'))
    url = 'https://api.doppler.com/v3/configs/config/secrets/download?format=%s' % format
    headers = {'User-Agent': 'python-doppler-env', 'Authorization': auth_header}
    request = urllib.request.Request(url, headers=headers)
    
    try:
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')
    except urllib.error.HTTPError as err:
        print('Doppler API Error: %s' % err)
        print_debug_info()


if os.environ.get('DOPPLER_ENV') is not None:    
    if(os.environ.get('DOPPLER_TOKEN')):
        print('DOPPLER_ENV and DOPPLER_TOKEN environment variable set. Fetching secrets from Doppler API.\n')
        env_vars = fetch_api(os.environ.get('DOPPLER_TOKEN'), format='env')
    else:
        print('DOPPLER_ENV environment variable set. Fetching secrets using Doppler CLI.\n')
        env_vars = fetch_cli()
    
    load_dotenv(stream=io.StringIO(env_vars))
