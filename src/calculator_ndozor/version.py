import subprocess

def get_version():
    try:
        # Get version from git tag
        version = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()
        # Remove 'v' prefix if present
        if version.startswith('v'):
            version = version[1:]
        return version
    except:
        return '0.0.1'  # Default version if no git tag is available

__version__ = get_version() 