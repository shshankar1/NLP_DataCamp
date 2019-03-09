Spacy installation in Windows doesn't seem to be straight forward.

Issues which I faced during installation and how I resolved that:

1. command "pip install spacy" ends with error "command cl.exe failed: No such file or directory"

Resolution:
 Make sure you have Microsoft Visual C++ 2017 redistribution installed.
 https://support.microsoft.com/en-in/help/2977003/the-latest-supported-visual-c-downloads

Some useful commands of python virtual environment (venv):
activate.bat: this is under python installation bin directory to activate venv.
deactivate.bat: this is under python installation bin directory to deactivate venv.