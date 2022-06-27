# doppler-env

The doppler-env package automates the injection of Doppler secrets as environment variables into any Python application and works in the terminal, PyCharm, and Visual Studio Code.
## Motivation

The Doppler CLI provides the easiest method of injecting secrets into your application:

```sh
doppler run -- python app.py
```

But when debugging with PyCharm or Visual Studio Code, a vendor-specific Python entry-point is used, preventing the Doppler CLI from acting as the application runner. At Doppler, we go to great lengths to [prevent secrets ending up on developer's machines](https://blog.doppler.com/how-to-prevent-secrets-from-ending-up-on-developers-machines) so downloading secrets to a .env file wasn't an option.

Thanks to Python's [Site configuration hook](https://docs.python.org/3/library/site.html) via a path configuration file, we can replicate the `doppler run` workflow by fetching the secrets via the Doppler CLI (recommended) or API and injecting into your Python application process prior to your code by being executed.

## Setup

Ensure you have [installed the Doppler CLI](https://docs.doppler.com/docs/enclave-installation) locally and have [created a Doppler Project](https://docs.doppler.com/docs/create-project). Then authorize the Doppler CLI to retrieve secrets from your workplace by running:

```sh
doppler login
```

Then install `doppler-env` in your local development environment or add it to the list of dev specific dependencies:

```sh
pip install doppler-env
```

## Configuration

First, define the `DOPPLER_ENV` environment variable in your IDE, editor, or terminal to trigger the injection of secrets:

```sh
export DOPPLER_ENV=1
```

Then configure which secrets to fetch for your application by either using the CLI in the root directory of your application:

```sh
doppler setup
```

Or set the `DOPPLER_PROJECT` and `DOPPLER_CONFIG` environment variables in your debug configuration within PyCharm or Visual Studio Code.

Now whenever the Python interpreter is invoked for your application, secrets will be injected prior to your application being run:

```sh
python app.py

# >> [doppler-env]: DOPPLER_ENV environment variable set. Fetching secrets using Doppler CLI
```

In restrictive environments where the use of the Doppler CLI isn't possible, set a `DOPPLER_TOKEN` environment variable with a [Service Token](https://docs.doppler.com/docs/service-tokens) to fetch secrets directly from the Doppler API:


```sh
python app.py

# >> [doppler-env]: DOPPLER_ENV and DOPPLER_TOKEN environment variable set. Fetching secrets from Doppler API
```

## Acknowledgements

This approach to injecting environment variables was inspired by [patch-env](https://github.com/caricalabs/patch-env).

## Issues

For any bug reports, issues, or enhancements, please [create a repository issue]().

# Support

You can get support in the [Doppler community forum](https://community.doppler.com/), find us on [Twitter](https://twitter.com/doppler), and for bugs or feature requests, [create an issue](https://github.com/DopplerHQ/python-doppler-env/issues/new) on the [DopplerHQ/python-doppler-env](https://github.com/DopplerHQ/python-doppler-env) GitHub repository.

If you need help, either use our in-product support or head over to the [Doppler Community Forum](https://community.doppler.com/) to get your questions answered by a member of the Doppler support team or 
