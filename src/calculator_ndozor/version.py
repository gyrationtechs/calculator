import subprocess
import re

def get_version():
    try:
        # Get version from git tag
        version = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()
        
        # Remove 'v' prefix if present
        if version.startswith('v'):
            version = version[1:]
            
        # Extract the base version (e.g., '0.0.3' from '0.0.3-1-g6e073de')
        match = re.match(r'^(\d+\.\d+\.\d+)', version)
        if match:
            return match.group(1)
        return version
    except:
        return '0.0.1'  # Default version if no git tag is available

__version__ = get_version() 