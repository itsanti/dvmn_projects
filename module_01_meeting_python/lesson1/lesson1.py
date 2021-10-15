from time import sleep
from earth_frames import earth_frames

for frame in earth_frames:
    print('\u001b[36;1m', frame, '\u001b[0m')
    print('\u001b[26A')
    sleep(0.5)
