@echo off
REM CodexPanel Bandwidth Reset Script for Windows
REM This script resets bandwidth usage for all domains in codexpanel

echo CodexPanel Bandwidth Reset Script
echo =================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with administrator privileges...
) else (
    echo Please run as administrator
    pause
    exit /b 1
)

REM Check if CodexPanel is installed
if not exist "C:\Program Files\codexpanel\bin\python.exe" (
    echo CodexPanel not found. Please ensure CodexPanel is installed.
    pause
    exit /b 1
)

echo Resetting bandwidth for all domains...
echo.

REM Run the bandwidth reset script
"C:\Program Files\codexpanel\bin\python.exe" "C:\Program Files\codexpanel\plogical\bandwidthReset.py" --reset-all

if %errorLevel% == 0 (
    echo.
    echo Bandwidth reset completed successfully!
    echo.
    echo To verify the reset, you can:
    echo 1. Check the CodexPanel logs
    echo 2. Check individual domain bandwidth in CodexPanel web interface
    echo 3. Check bandwidth metadata files
) else (
    echo.
    echo Bandwidth reset failed. Please check the logs for details.
    pause
    exit /b 1
)

echo.
echo Note: This script only resets the displayed bandwidth values.
echo The actual bandwidth calculation will resume from the current access logs.
echo For a complete reset, you may also need to clear access logs if desired.
pause
