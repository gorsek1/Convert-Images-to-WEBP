@echo off
echo Image to WebP Converter
echo =====================
echo.

:: Try to find Python using different methods
set PYTHON_CMD=

:: Try python command
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python
    goto :found_python
)

:: Try py command
py --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=py
    goto :found_python
)

:: Try common Python installation paths
if exist "C:\Python39\python.exe" (
    set PYTHON_CMD=C:\Python39\python.exe
    goto :found_python
)

if exist "C:\Python310\python.exe" (
    set PYTHON_CMD=C:\Python310\python.exe
    goto :found_python
)

if exist "C:\Python311\python.exe" (
    set PYTHON_CMD=C:\Python311\python.exe
    goto :found_python
)

if exist "C:\Program Files\Python39\python.exe" (
    set PYTHON_CMD="C:\Program Files\Python39\python.exe"
    goto :found_python
)

if exist "C:\Program Files\Python310\python.exe" (
    set PYTHON_CMD="C:\Program Files\Python310\python.exe"
    goto :found_python
)

if exist "C:\Program Files\Python311\python.exe" (
    set PYTHON_CMD="C:\Program Files\Python311\python.exe"
    goto :found_python
)

if exist "%LOCALAPPDATA%\Programs\Python\Python39\python.exe" (
    set PYTHON_CMD="%LOCALAPPDATA%\Programs\Python\Python39\python.exe"
    goto :found_python
)

if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    set PYTHON_CMD="%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto :found_python
)

if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set PYTHON_CMD="%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    goto :found_python
)

:python_not_found
echo ERROR: Python was not found on your system.
echo Please install Python from https://www.python.org/downloads/
echo.
echo After installing Python, run this batch file again.
echo.
pause
exit /b 1

:found_python
echo Found Python: %PYTHON_CMD%
echo.

:: Install Pillow if needed
echo Checking for required packages...
%PYTHON_CMD% -c "import PIL" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing Pillow package...
    %PYTHON_CMD% -m pip install pillow
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to install Pillow. Please install it manually:
        echo %PYTHON_CMD% -m pip install pillow
        pause
        exit /b 1
    )
)

echo.
echo Running image conversion script...
echo.

:: Run the conversion script
%PYTHON_CMD% image_convert_to_webp.py 85

echo.
echo Conversion process completed!
pause 