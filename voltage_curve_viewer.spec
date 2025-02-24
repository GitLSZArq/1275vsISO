# voltage_curve_viewer.spec
block_cipher = None
from PyInstaller.utils.hooks import copy_metadata

# Copy the metadata for streamlit and importlib-metadata
datas = copy_metadata('streamlit') + copy_metadata('importlib_metadata')

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,  # Include the copied metadata
    hiddenimports=[
        'plot_functions',
        'plotly',
        'numpy',
        'streamlit',
        'importlib.metadata',
        'importlib.resources',
        'streamlit.runtime.scriptrunner',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Voltage_Standard_Curve_Viewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='Voltage_Standard_Curve_Viewer'
)
