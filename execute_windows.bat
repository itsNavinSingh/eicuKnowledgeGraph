@echo off
setlocal enabledelayedexpansion

:: Create a virtual environment
echo Creating virtual environment...
python -m venv venv

:: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install dependencies
echo Installing required Python packages...
pip install -r requirements.txt

:: Prompt user for input directory
echo Enter the input directory path:
set /p input_path=

:: Create a result directory
set result_dir=result
if not exist "%result_dir%" mkdir "%result_dir%"

:: Loop through all Python files in the current directory
for %%f in (*.py) do (
    echo %%f execution started
    python "%%f" "%input_path%"
    echo %%f execution completed
)

echo All scripts executed.
pause

:: excution command
:: ./execute_windows.bat