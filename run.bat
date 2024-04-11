@echo off

python --version > nul 2>&1

if errorlevel 9009 (
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe', 'python-3.11.0-amd64.exe')"
    python-3.11.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
)

python -m venv %~dp0.venv
python -m pip install mss
python -m pip install pynput
python -m pip install opencv-python
python main.py

pause