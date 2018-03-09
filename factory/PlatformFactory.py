import platform
from platforms.ubuntu import Ubuntu
from platforms.fedora import Fedora

class PlatformFactory:
	@staticmethod
	def create(version):
		print "DEBUG: "+version
		if "Ubuntu" in version:
			print "DEBUG: Ubuntu"
			return Ubuntu(version)
		elif "Fedora" in version:
			return Fedora(version)
		else:
			return None

