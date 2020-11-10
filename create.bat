@echo off

set fn=%1
set flag1=%2
set flag2=%3
cd /d %~dp0

If "%1"=="" (
    echo Must Provide a folder name
) else (
    python remote.py %fn% %flag1% %flag2%
    )