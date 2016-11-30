import time, math, json
from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.mp_settings import MPSetting

# Sciezka do biblioteki interop
import sys
#sys.path.append('/home/krzysiu/interop/client/tools')
sys.path.append('/home/krzysiu/MAVProxy/interop')
sys.path.append('/usr/lib/python2.7')
sys.path.append('/usr/lib/python3.5')

INTEROP_URL = 'http://localhost:8000'
INTEROP_USERNAME = 'testuser2'
INTEROP_PASSWORD = 'testpass'
POLL_SEC = 0.1
PRINT_SEC = 3


try:
    from interop import AsyncClient	
    from interop import Telemetry
    import interop
except ImportError as e:
    raise ImportError(
        'Failed to import interop libraries. Have you added the libs to '
        'the path? Error: %s' % e)


client = interop.AsyncClient(url=INTEROP_URL,username=INTEROP_USERNAME,password=INTEROP_PASSWORD)
mission = client.get_missions()
#stationary_obstacles, moving_obstacles = client.get_obstacles()

print len(mission.result())
for a in (mission.result()):
	print a


class Misje(mp_module.MPModule):
  def __init__(self, mpstate):
    super(Misje, self).__init__(mpstate, "misje", "misje module")
    self.client = AsyncClient(INTEROP_URL, INTEROP_USERNAME, INTEROP_PASSWORD)

  def mavlink_packet(self, m):
	'''handle a mavlink packet'''
		



def init(mpstate):
	missions = client.get_missions()
	print missions
	return Misje(mpstate)
