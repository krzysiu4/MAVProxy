'''module template'''
import time, math
from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.mp_settings import MPSetting

import sys
sys.path.append('/home/krzysiu/interop/client/tools')

INTEROP_URL = 'http://localhost:8000'
INTEROP_USERNAME = 'testuser'
INTEROP_PASSWORD = 'testpass'
POLL_SEC = 0.1
PRINT_SEC = 3

try:
    from interop import AsyncClient
    from interop import Telemetry
except ImportError as e:
    raise ImportError(
        'Failed to import interop libraries. Have you added the libs to '
        'the path? Error: %s' % e)



class Telemetria(mp_module.MPModule):
  def __init__(self, mpstate):
    super(Telemetria, self).__init__(mpstate, "telemetria", "telemetria module")
    self.add_command('zrobCos', self.cmd_zrobCos, "zrobCos commands")
    self.client = AsyncClient(INTEROP_URL, INTEROP_USERNAME, INTEROP_PASSWORD)

  def mavlink_packet(self, m):
	'''handle a mavlink packet'''
	if m.get_type() == 'GLOBAL_POSITION_INT':
		telemetry = Telemetry(float(m.lat)/10000000, float(m.lon)/10000000, float(m.alt)/1000, float(m.hdg)/100)
		self.client.post_telemetry(telemetry)		

  def cmd_zrobCos(self,args):
	print "Niby co"

def init(mpstate):
	'''initialise module'''
	return Telemetria(mpstate)
