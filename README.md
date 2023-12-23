<p align="center"><img src="Images/GoonLogo.png" width="26%" height="26%"></p>

- $${\color{red}FAILS TO ALARM AFTER X AMOUNT OF TIME - DON'T TRUST YET - W.I.P.}$$

# Description
While playing Eve Online and ratting in nullsec, sure would be nice if ships from over a thousand years in the future, could warn you when an unknown contact enters the system, much like our ships today can do :P  
This program opens to the system tray, takes a screenshot once per second, looks for the neutral logo, and sounds an alarm (sonar sound) when the logo is found.  
Right click on the system tray icon and select exit to terminate the program.  
Tested on Windows 10.

# Dependencies
- $${\color{red}pyinstaller v6 creates a false positive for malware!}$$
```pip install pyautogui
pip install numpy
pip install pillow
pip install playsound
pip install opencv-python-headless
pip install pystray
pip install pyinstaller==5.13.2
```

# Compile
`pyinstaller LocalAlarm.spec`  
Executable can be found at `EveLocalNeutralAlarm\dist\LocalAlarm.exe`