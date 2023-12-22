# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.win32.versioninfo import VSVersionInfo, FixedFileInfo, StringStruct, StringTable, StringFileInfo, VarStruct, VarFileInfo

version_info = VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(0, 9, 2, 0),
        prodvers=(0, 9, 2, 0),
        mask=0x3f,
        flags=0x0,
        OS=0x4,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo([
            StringTable(
                '040904B0',
                [
                    StringStruct('CompanyName', 'Graham Pinkston'),
                    StringStruct('FileDescription', 'Eve Local Neutral Alarm'),
                    StringStruct('FileVersion', '0.9.2.0'),
                    StringStruct('InternalName', 'Graham Pinkston'),
                    StringStruct('OriginalFilename', 'LocalAlarm.exe'),
                    StringStruct('ProductName', 'Eve Local Neutral Alarm'),
                    StringStruct('ProductVersion', '0.9.2.0')
                ]
            )
        ]),
        VarFileInfo([VarStruct('Translation', [1033, 1200])])
    ]
)

a = Analysis(
    ['LocalAlarm.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Images/GoonLogo.png', 'Images'),
        ('Images/Neutral24BitNormal.bmp', 'Images'),
        ('Images/Neutral24BitCompact.bmp', 'Images'),
        ('Sounds/sonar.wav', 'Sounds')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LocalAlarm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version=version_info,
)
