from cx_Freeze import setup, Executable

# Define build options
build_options = {
    'packages': ['numpy', 'plotly', 'streamlit', 'importlib.metadata'],
    'include_files': ['plot_functions.py'],
}

# Define the executable
executables = [Executable('main.py', target_name='Voltage_Standard_Curve_Viewer.exe')]

# Setup configuration
setup(
    name='Voltage_Standard_Curve_Viewer',
    version='1.0',
    description='Voltage Standard Curve Viewer Application',
    options={'build_exe': build_options},
    executables=executables
)
