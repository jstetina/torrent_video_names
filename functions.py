import re

from torrent_video_names.patterns import STOP_PATTERNS
from torrent_video_names.extensions import VIDEO_EXTENSIONS

def rename(file:str):
    file_name = " ".join(file.split(".")[:-1])
    file_name = file_name.split(" ")

    file_extension = file.split(".")[-1]
    
    # Skip non-video files
    if file_extension.lower() not in VIDEO_EXTENSIONS:
        return False
    
    STOP_REACHED = False
    words = []
    for word in file_name:
        for pattern in STOP_PATTERNS:
            if re.match(pattern, word.lower()):
                STOP_REACHED = True
                break
        if STOP_REACHED:
            break
        words.append(word)
    
    return " ".join(words) + "." + file_extension
