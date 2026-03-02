#!/usr/bin/env python3
"""
Meeting Intelligence Agent - Linux Startup Script
This script starts the application with proper Linux configuration
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Start the Meeting Intelligence Agent application"""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Set environment variables for Linux
    os.environ['PYTHONPATH'] = str(script_dir)
    os.environ['APP_ENV'] = 'production'
    os.environ['APP_ENVIRONMENT'] = 'production'
    
    print(" Starting Meeting Intelligence Agent...")
    print(f" Working directory: {script_dir}")
    print(f" Python path: {os.environ.get('PYTHONPATH')}")
    
    try:
        # Start the application using uvicorn
        cmd = [
            sys.executable, '-m', 'uvicorn',
            'src.api.main:app',
            '--host', '0.0.0.0',
            '--port', '8000',
            '--workers', '1',  # Single worker for e2-small instance
            '--log-level', 'info'
        ]
        
        print(f" Running command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n Application stopped by user")
    except Exception as e:
        print(f" Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
