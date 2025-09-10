import os

def load_env_file(filepath=".env"):
    """Load environment variables from a file into os.environ."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found.")
    with open(filepath) as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

def environment_variables(filepath=".env"):
    """Parse environment variables from a file and return as a dict (does not set os.environ)."""
    env_dict = {}
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found.")
    with open(filepath) as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.strip().split('=', 1)
                env_dict[key] = value
    return env_dict

def get_environment_variable(var_name, filepath=".env"):
    """Get a single environment variable value from a file without setting os.environ."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found.")
    with open(filepath) as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.strip().split('=', 1)
                if key == var_name:
                    return value
    raise KeyError(f"{var_name} not found in {filepath}.")
