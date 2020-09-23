@echo off

set fn=%1
set flag=%2
cd /d %-dp0

if "%1"=="" (
    echo Must Provide a folder name
)else(
    python main.py %fn% %flag%
    )