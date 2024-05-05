from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "PIL", "PySimpleGUI"]}

setup(
    name = "TileSeparator",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base="Win32GUI")]
)