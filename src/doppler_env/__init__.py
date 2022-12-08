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
import urllib.parse

from dotenv import load_dotenv

LOGGING_ENABLED = True if os.environ.get('DOPPLER_ENV_LOGGING') is not None else False


def log(message):
    if LOGGING_ENABLED:
        print('[doppler-env]: {}'.format(message))


def print_debug_info(doppler_token=None, project=None, config=None):
    doppler_token and log('Token: {}.*****'.format('.'.join(doppler_token.split('.')[:-1])))
    project and log('Project: {}'.format(project))
    config and log('Config: {}'.format(config))
    log('Python path: {}'.format(sys.executable))
    log('Working directory: {}'.format(os.getcwd()))


def fetch_cli():
    command = os.environ.get('DOPPLER_ENV_COMMAND', 'doppler secrets download --no-file --format env')

    try:
        subprocess.check_output('doppler', stderr=subprocess.STDOUT).decode('utf-8')
    except FileNotFoundError:
        log('The Doppler CLI is not installed. See https://docs.doppler.com/docs/install-cli')
        return

    # If non-zero exit code, catch Python exception so only output is stderr from Doppler CLI
    try:
        return subprocess.check_output(command.split()).decode('utf-8')
    except subprocess.CalledProcessError:
        print_debug_info()


def fetch_api(doppler_token, project=None, config=None):
    if ('dp.ct' in doppler_token or 'dp.pt' in doppler_token) and (project is None or config is None):
        log(
            'Error: DOPPLER_PROJECT and DOPPLER_CONFIG environment variables must be set if using a CLI or Personal Token'
        )
        print_debug_info()
        return

    auth_header = b'Basic %s' % b64encode('{}:'.format(doppler_token).encode('ascii'))
    headers = {'User-Agent': 'python-doppler-env', 'Authorization': auth_header}
    params = {'format': 'env'}
    if project and config:
        params.update({'project': project, 'config': config})
    url = 'https://api.doppler.com/v3/configs/config/secrets/download?{}'.format(urllib.parse.urlencode(params))

    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')
    except urllib.error.HTTPError as err:
        log('Doppler API Error {}'.format(err.read().decode('utf-8')))
        print_debug_info(doppler_token, project, config)


if os.environ.get('DOPPLER_ENV') is not None:
    doppler_token = os.environ.get('DOPPLER_TOKEN')

    if doppler_token:
        log('DOPPLER_ENV and DOPPLER_TOKEN environment variable set. Fetching secrets from Doppler API')
        env_vars = fetch_api(
            os.environ.get('DOPPLER_TOKEN'), os.environ.get('DOPPLER_PROJECT'), os.environ.get('DOPPLER_CONFIG')
        )
    else:
        log('DOPPLER_ENV environment variable set. Fetching secrets using Doppler CLI')
        env_vars = fetch_cli()

    load_dotenv(stream=io.StringIO(env_vars))
