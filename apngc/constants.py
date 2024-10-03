import os

# DEFINE GLOBALS
ROOT = os.path.dirname(os.path.dirname(__file__))
PACKAGE = os.path.dirname(__file__)
SETTINGS_PATH = os.path.join(ROOT, "settings")

# EXECUTABLES
if os.name == "nt":  # Windows
    BIN = os.path.join(ROOT, "bin", "win")
    FFMPEG_PATH = os.path.join(BIN, "ffmpeg", "bin")
else:  # macOS or Linux
    BIN = os.path.join(ROOT, "bin", "mac")
    FFMPEG_PATH = os.path.join(BIN, "ffmpeg")

APNGASM_PATH = os.path.join(BIN, "apngasm")
