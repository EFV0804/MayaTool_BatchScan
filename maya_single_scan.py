import glob
import subprocess
import logging
from datetime import datetime

def run(maya_exe, file_path):
    logging.warning('Parsing maya scene file paths')
    maya_exe_path = maya_exe

    logging.warning('Scanning files')
    subprocess.run([maya_exe_path, '-batch', '-file', "{file_path}", "-command", "evalDeferred (\"loadPlugin MayaScanner; MayaScan;\")".format(file_path=file_path)])

    logging.warning('Scanned and cleaned all files')