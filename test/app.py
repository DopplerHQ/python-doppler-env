import os

print(
    '\n'.join(
        [f'{key} = {val}' for (key, val) in os.environ.items() if key.find('DOPPLER_') >= 0 and key not in ['DOPPLER_ENV', 'DOPPLER_TOKEN']]
    )
)
