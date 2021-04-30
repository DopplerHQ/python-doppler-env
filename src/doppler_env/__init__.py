"""
Imported by doppler_env.pth Automatically inject Doppler secrets as environment variables when spawning a Python process if the `DOPPLER_ENV` environment variable is set
"""
import os


def doppler_secrets_env():
    import io
    import subprocess
    import logging
    from dotenv import load_dotenv

    DOPPLER_ENV_COMMAND = os.environ.get(
        'DOPPLER_ENV_COMMAND', 'doppler secrets download --no-file --format env'
    )
    process = subprocess.run(DOPPLER_ENV_COMMAND, shell=True, capture_output=True)
    if process.returncode != 0:
        logging.error('Doppler secrets fetch failed {process.returncode}')
        if process.stderr:
            logging.error(process.stderr)
        if process.stdout:
            logging.error(process.stdout)
    else:
        config = io.StringIO(process.stdout.decode('utf-8'))
        load_dotenv(stream=config)


if os.environ.get('DOPPLER_ENV') is not None:
    doppler_secrets_env()
