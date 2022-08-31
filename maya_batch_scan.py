import glob
import subprocess
import logging
from datetime import datetime
import os

def run():

    maya_exe_path = "C:/Program Files/Autodesk/Maya2022/bin/maya.exe"
    projet_search = "Z:/*"
    projects_path = glob.glob(projet_search, recursive=True)
    projects = []
    excluded = []

    # Get project name from each project paths
    for project in projects_path:
        if os.path.basename(project) not in excluded:
            projects.append(os.path.basename(project))

    for project in projects:
        logging.warning('Parsing maya scene file paths for {}'.format(project))

        # Parse and collect all Maya scenes
        pattern_ma = "Z:/{}/03_production/**/*.ma".format(project)
        pattern_mb = "Z:/{}/03_production/**/*.mb".format(project)
        maya_scenes = glob.glob(pattern_ma, recursive=True)
        maya_scenes += glob.glob(pattern_mb, recursive=True)

        # Open log file, and run the Maya scan as subprocess
        logging.warning('Scanning filesfor {}'.format(project))
        with open('U:/mesDocuments/dev/maya_batch_scan/logs.txt', 'a') as logs:
            for scene in maya_scenes:
                logging.warning('Scanning: {}'.format(scene))
                logs.write(datetime.now().strftime('%H:%M:%S') + ' : ' + scene + '\n')
                subprocess.run([maya_exe_path, '-batch', '-file', "'{scene}'".format(scene=scene), "-command",
                                "evalDeferred (\"loadPlugin MayaScanner; MayaScan;\")"],
                stdout=logs, text=True, check=True, timeout=300)

    logging.warning('Scanned and cleaned all files')