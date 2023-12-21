# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['LocalAlarm.py'],
    pathex=[],
    binaries=[],
    datas=[
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
)
