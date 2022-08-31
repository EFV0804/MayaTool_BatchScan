# Maya Batch Scan
This scripts allows to scan a maya scenes in batch to detect corrupt one, and clean them. It's designed to parse through all files given a specific search pattern

To run the script, from a Python console:


        import sys
        sys.path.append('{location on disk of this module}')
        import maya_batch_scan
        maya_batch_scan.run()


Some parts of the script are studio specific, such as the Maya exe path, and the search pattern to parse through each project.

A log file is updated with the time and path of the scenes that have been scanned.

# Maya Single Scan
This script allows to scan and clean a single Maya scene.

To run, from a Python console:

        import sys
        sys.path.append('{location on disk of this module}')
        import maya_single_scan
        maya_single_scan.run({maya_exe_path}, {file_path})