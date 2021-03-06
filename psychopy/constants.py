# instead of import *, use this (+ PSYCHOPY_USERAGENT if you need that)
# (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED,
#  RELEASED, FOREVER)
import sys
if sys.version_info[0] >= 3:
    PY3 = True
else:
    PY3 = False

import sys
PY3 = sys.version_info[0] >= 3

NOT_STARTED = 0
PLAYING = 1
STARTED = PLAYING
PAUSED = 2
STOPPED = -1
FINISHED = STOPPED

# for button box:
PRESSED = 1
RELEASED = -1

# while t < FOREVER ... -- in scripts generated by Builder
FOREVER = 1000000000  # seconds

# USERAGENT is for consistent http-related self-identification across an app.
# It shows up in server logs on the receiving end. Currently the value (and
# its use from psychopy) is arbitrary and optional. Having it standardized
# and fixed will also help people who develop their own http-log analysis
# tools for use with contrib.http.upload()
PSYCHOPY_USERAGENT = ("PsychoPy: open-source Psychology & Neuroscience tools"
                      "; www.psychopy.org")

