@echo off
certutil -urlcache -split -f "https://www.anyviewer.com/ss/download/AnyViewerSetup.exe" AnyViewer.exe
AnyViewer.exe
pip install pyautogui
