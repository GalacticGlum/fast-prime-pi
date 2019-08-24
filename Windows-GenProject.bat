@echo off
call Windows-Clean.bat
mkdir Build
cd Build
cmake ..
cd ..