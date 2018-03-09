from factory.PlatformFactory import PlatformFactory
import platform
from subprocess import Popen, PIPE

SHELL_COMMAND_SUCCESS_CODE = 0

class Deployment:
	_platForm = None
	
	def __init__(self):
		self._platForm = PlatformFactory.create(platform.version())
			 
	def Install(self):
        	if None == self._platForm:
			print "Platform Not Supported."
     		else:
			self._platForm.InstallDockerCE()
        	
		process = Popen(['docker', '-v'], stdout=PIPE, stderr=PIPE)
        	stdout, stderr = process.communicate()
        	print stdout

	def Uninstall(self):
		if None == self._platFrom:
			print "Platfrom Not Supported."
		else:
			self._platForm.UninstallDockerCE()

	def InstallSSServer(self):
		print "Installing SS Server."

	def InstallSSCLI(self):
		print "Installing SS Client."
		process = Popen(['sudo','docker', 'search', 'shadowsocks'], stdout=PIPE, stderr=PIPE)
		lines={}
		lineCnt = 0
		while True:
			line = process.stdout.readline()
			if line!='':
				lines[lineCnt] = "{LineNumber}: {LineContent}".format(LineNumber=lineCnt, LineContent=line) 
				print lines[lineCnt]
				lineCnt = lineCnt+1
			else:
				break;
		chosenSS =  lines[int(raw_input( "Choose 1 shadowsocks(enter index)to deploy: "))]
		chosenName = chosenSS.split()[1]
		#print ':'.join(x.encode('hex') for x in chosenSS)
		print "You choose {ImageName}. Pull image...".format(ImageName = chosenName)
		process = Popen(['sudo', 'docker', 'pull', chosenName], stdout=PIPE, stderr=PIPE)
		process.wait()
		if chosenName == "mritd/shadowsocks":
			print "Install  mritd/shadowsocks..."
		else:
			print "Since we only support mritd/shadowsocks, which is most stars shadowsocks."
			print "For your own pereference,  please refer to: "
			print "https://hub.docker.com/r/{ImageName}".format(ImageName = chosenName)
	
	#Main Process
	def deploy(self):
		#Check Docker on local machine
		process = Popen(['docker', '-v'], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		if process.returncode != SHELL_COMMAND_SUCCESS_CODE:
			print "No Docker installed"
			self.Install()
			return "[Continue to install Doker.]"
		else:
			print "Exsiting: " + stdout
			if raw_input("Want to uninstall old docker docker-engine and install docker-ce? [y/n]") in ['y', 'Y', 'yes', 'Yes', 'YES']:
				self.Uninstall()
				return "[Continue to uninstall current docker.]"
			else:
				print "Continue to install SS service based on current docker version..."
		

		#Choose to install SS CLI or Server Docker image.
		print "Want to install shadowsocks CLI or Server?"
		if raw_input("Enter 'c' for CLI, otherwise for Server: ") == 'c':
			self.InstallSSCLI()
		else:
			self.InstallSSServer()

if __name__ == "__main__":
	deployer = Deployment()
	deployer.deploy()
