def load_env(filepath : str):
    env = {}
    with open(f'{filepath}', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                env[key.strip()] = value.strip()
    return env