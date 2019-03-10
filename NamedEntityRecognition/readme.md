Spacy installation in Windows doesn't seem to be straight forward.

Issues which I faced during installation and how I resolved that:

1. command "pip install spacy" ends with error "command cl.exe failed: No such file or directory"

Resolution:
 Make sure you have Microsoft Visual C++ 2017 redistribution installed.
 https://support.microsoft.com/en-in/help/2977003/the-latest-supported-visual-c-downloads

Also run below command from terminal:
pip install spacy-nightly
get out of venv
manually goto venv Scripts directory and then execute below
python -m spacy download en


Some useful commands of python virtual environment (venv):
activate.bat: this is under python installation bin directory to activate venv.
deactivate.bat: this is under python installation bin directory to deactivate venv.

Good starting point for NER:
https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

https://www.crossplatform.net/getting-started-with-spacy/
