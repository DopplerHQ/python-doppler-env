# doppler-env

Inject Doppler secrets as environment variables into your Python application during local development. Provides debugging support in PyCharm, Visual Studio Code, and other IDEs and editors.

Inspired by [patch-env](https://github.com/caricalabs/patch-env).

> NOTE: This package should be used during local development only. It is not suitable, recommended, or supported for production usage.

## How it works

Debugging in IDE's such as PyCharm and Visual Studio Code do not allow the Doppler CLI to be used as the process runner for Python as they use their own Python debugger entrypoint. This often forces developers to resort to insecure practices such saving Doppler secrets to an `.env` file during development, the very problem Doppler was created to prevent.

The **doppler-env** package provides a solution in the form of a [site hook that is run at Python startup](https://docs.python.org/3/library/site.html).

If the `DOPPLER_ENV` environment variable is set, the package will call out to the Doppler CLI to fetch secrets for the project and inject them as environment variables into the process spwawned by the commmand line or IDE with your secrets never touching the file system.

## Requirements

Ensure the [Doppler CLI](https://docs.doppler.com/docs/enclave-installation) is installed and you have [created a project in Doppler](https://docs.doppler.com/docs/enclave-project-setup).

Then authenticate the Doppler CLI so it can retrieve secrets from your workplace:

```sh
doppler login
```

## Getting started

1. If you haven't already, open a new terminal window, change into the repository folder, then configure the Doppler CLI by selecting the project and config for development:

```sh
doppler setup
```

2. Install `doppler-env` in your local development environment:

```sh
pip install doppler-env
```

3. On the command line or in your editor, set the environment variable `DOPPLER_ENV` to trigger injecting secrets as environment variables:

```sh
export DOPPLER_ENV=1
```

4. Run or debug your application as per normal:

```sh
python src/app.py
```
