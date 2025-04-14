import subprocess
import re

def get_version():
    try:
        # First, fetch all tags
        subprocess.check_output(['git', 'fetch', '--tags'], stderr=subprocess.STDOUT)
        
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
    except subprocess.CalledProcessError as e:
        print(f"Error getting version: {e}")
        return '0.0.3'  # Default version if git commands fail
    except Exception as e:
        print(f"Unexpected error: {e}")
        return '0.0.3'  # Default version for any other errors

__version__ = get_version() 