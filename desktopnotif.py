import time
import notify2
from news import topstories
ICON_PATH = "PUT FULL PATH TO ICON IMAGE HERE"

newsitems = topstories()
notify2.init(" news notifier")

n = notify2.Notifications(None, icon = ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(1000)
for newsitem in newsitems:
    n.update(newsitem['title'], newsitem['description'])
    n.show()
    time.sleep(15)