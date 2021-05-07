"""
Imported by doppler_env.pth Automatically inject Doppler secrets as environment variables when spawning a Python process if the `DOPPLER_ENV` environment variable is set
"""
import os


def doppler_secrets_env():
    import io
    import subprocess
    from dotenv import load_dotenv

    DOPPLER_ENV_COMMAND = os.environ.get(
        'DOPPLER_ENV_COMMAND', 'doppler secrets download --no-file --format env'
    )

    # If non-zero exit code, catch Python exception so only output is stderr from Doppler CLI
    try:
        env_vars = subprocess.check_output(DOPPLER_ENV_COMMAND.split()).decode('utf-8')
    except subprocess.CalledProcessError as err:
        exit(err.returncode)

    load_dotenv(stream=io.StringIO(env_vars))


if os.environ.get('DOPPLER_ENV') is not None:
    doppler_secrets_env()
