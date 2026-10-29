"""Print the current Unix timestamp and date in the subject's format."""

import time

TimeSeconds = time.time()

print(
    f"Seconds since January 1, 1970: {TimeSeconds:,.4f} "
    f"or {TimeSeconds:.2e} in scientific notation"
)
print(time.strftime("%b %d %Y"))
