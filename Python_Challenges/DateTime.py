from datetime import datetime, timedelta, timezone
from pytz import timezone

format = "%H:%M:%S %Z"

print("Current Time:")

portland = datetime.now(timezone('America/Los_Angeles'))
print("Portland:",portland.strftime(format))

newyork = datetime.now(timezone('America/New_York'))
print("NYC:",newyork.strftime(format))

london = datetime.now(timezone('Europe/London'))
print("London:",london.strftime(format))

if portland.hour > 8 and portland.hour < 17:
    print("The Portland branch is open")
else:
    print("The Portland branch is closed")

if newyork.hour > 8 and newyork.hour < 17:
    print("The NYC branch is open")
else:
    print("The NYC branch is closed")

if london.hour > 8 and london.hour < 17:
    print("The London branch is open")
else:
    print("The London branch is closed")




