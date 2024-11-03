import platform
import sys

def get_python_info():
    print("Python Environment Information:")
    print(f"Python Version: {platform.python_version()}")
    print(f"Implementation: {platform.python_implementation()}")
    print(f"System: {platform.system()}")
    print(f"Path: {sys.executable}")