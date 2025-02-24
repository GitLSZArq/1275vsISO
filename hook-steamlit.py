from PyInstaller.utils.hooks import copy_metadata

# Copy the metadata for streamlit
datas = copy_metadata('streamlit')
