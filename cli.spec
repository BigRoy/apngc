# -*- mode: python ; coding: utf-8 -*-

import platform

if platform.system().lower() == "windows":
    bin_path = "bin/win"
    icon = "apngc/ui/icons/apngc.ico"
elif platform.system().lower() == "darwin":
    bin_path = "bin/mac"
    icon = "apngc/ui/icons/apngc.ico"


a = Analysis(
    ["cli.py"],
    pathex=["apngc"],
    binaries=[],
    datas=[
        ("apngc/ui", "apngc/ui"),
        (bin_path, bin_path),
        ("apngc/settings", "apngc/settings"),
    ],
    hiddenimports=["click", "PySide6"],
    hookspath=["hooks"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    **{"onefile": True, "noconfirm": True},
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="apngc",
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    icon=icon,
)

if platform.system() == "Darwin":
    info_plist = {"addition_prop": "additional_value"}
    app = BUNDLE(
        exe,
        name="apngc.app",
        bundle_identifier=None,
        info_plist=info_plist,
        icon=icon,
    )
