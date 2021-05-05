# doppler-env

Inject Doppler secrets as environment variables into your Python application during local development with built-in debugging support for PyCharm and Visual Studio Code.

## How it works

Debugging support in PyCharm and Visual Studio Code is provided by a vendor-specific Python entry-point which prevents the Doppler CLI from being used to directly inject secrets.

This limitation may force developers to use insecure practices such as saving secrets to an unencrypted `.env` file—the issue Doppler was created to prevent.

Simply set the `DOPPLER_ENV` environment variable, and the `doppler-env` package will fetch your secrets using the Doppler CLI, injecting them as environment variables before executing your Python code.

All this while ensuring secrets never touch the file system.

## Requirements

Ensure you have installed the [Doppler CLI](https://docs.doppler.com/docs/enclave-installation) and [created a project in the Doppler dashboard](https://docs.doppler.com/docs/enclave-project-setup).

Then in a local terminal, authorize the Doppler CLI to retrieve secrets from your workplace:

```sh
doppler login
```

## Getting started

1. If you haven't already, open a new terminal window, change into the repository folder, then configure the Doppler CLI by selecting the project and config to supply secrets for:

```sh
doppler setup
```

2. Install `doppler-env` in your local development environment:

```sh
pip install doppler-env
```

3. Define the `DOPPLER_ENV` environment variable in your IDE, editor, or terminal:

```sh
export DOPPLER_ENV=1
```

4. Run or debug your application in your IDE, editor, or terminal:

```sh
python src/app.py
```

## Acknowledgements

This approach to injecting environment variables was inspired by [patch-env](https://github.com/caricalabs/patch-env) and customized to be Doppler specific.

## Issues

For any bug reports, issues, or enhancements, please [create a repository issue](https://github.com/DopplerHQ/python-doppler-env/issues/new).

## Support

Paid subscribers can use in-product support while those on Doppler's free community plan can receive help in our [Community forum](https://community.doppler.com/).
