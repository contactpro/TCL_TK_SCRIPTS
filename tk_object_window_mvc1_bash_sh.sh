#!/bin/bash

# Uncomment the !! because the editor screen color hides comments

# Specify Display
# export DISPLAY=172.16.0.1:1
# export DISPLAY=172.16.0.1:0
echo "  "
echo "... export DISPLAY CHIPCODER:0.0 ... "
echo "... export DISPLAY CHIPCODER:0.0 ... "
echo "... export DISPLAY CHIPCODER:0.0 ... "
export DISPLAY=CHIPCODER:0.0
echo "  "

# Generate the directory name in the format "workpython-YEAR-MONTH-DAY"

LINUX_DIRECTORY_NAME="LINUX_DIRECTORY_NAME"
MACOS_DIRECTORY_NAME="MACOS_DIRECTORY_NAME"
WINDOWS_DIRECTORY_NAME="WINDOWS_DIRECTORY_NAME"
DATE_VAR="Date: $(date +%Y-%m-%d)"

echo "   "
echo "-------------------------------------------------------------------------"
echo "   Running tk_object_window_mvc1.py to create tkinter object window. "
echo "-------------------------------------------------------------------------"
echo "$LINUX_DIRECTORY_NAME"
echo "$MACOS_DIRECTORY_NAME"
echo "$WINDOWS_DIRECTORY_NAME"
echo "$DATE_VAR"
echo "-------------------------------------------------------------------------"
pwd
ls
pwd
# Display python version
python3 --version
pwd
# Run the tk_object_window_mvc1 script
python3 tk_object_window_mvc1.py
pwd
# Run the Python script
# python3 uvm_builder_python.py
pwd


