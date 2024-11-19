import platform

def get_device_info():
    device_info = {
        'platform': platform.system(),
        'platform_version': platform.release(),
        'architecture': platform.machine(),
        'python_version': platform.python_version(),
    }
    return device_info

# Initialize device information
DEVICE_INFO = get_device_info()