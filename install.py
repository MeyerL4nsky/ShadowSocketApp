from subprocess import Popen, PIPE
import platform

SHELL_COMMAND_SUCCESS_CODE = 0

def How2Install():
        version = platform.version()
	if "Ubuntu" in version:
		print "Install Docker on Ubuntu, following:"
		print "1. Set up the repository:"\
		      "  sudo apt-get update\n"\
		      "  sudo apt-get install apt-transport-https ca-certificates curl software-properties-common\n"\
                      "  curl -fsSL http://download.docker.com/linux/ubuntu/gpg | sudo apt=key add -\n"\
		      "  sudo apt-key fingerprint 0EBFCD88\n"\
                      "  sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) satble'\n"\
		      "2. Install Docker form repo:\n"\
                      "  sudo apt-get update\n"\
                      "  sudp apt-get install docker-ce\n"\
		      "3. Start Docker:\n"\
                      " Auto Run on Ubuntu.\n"\
                      "4. Verify:\n"\
		      " sudo docker run hello-world\n"\
                      "5. More:\n"\
                      "https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1\n"
 
	elif "Fedora" in version:
		print "Installing Docker on Fedora, follwoing:"
		print "1. Set up the repository:\n"\
		      " sudo dnf -y install dnf-plugins-core\n"\
		      " sudo dnf config-manager --add-repo https://download.docker.com/linux/docker-ce.repo\n"\
                      "2. Install Docker from repo:\n"\
                      " sudo dnf install docker-ce\n"\
                      " Then accept the fingerprint\n"\
		      "3. Start Docker:\n"\
		      " sudo systemctl start docker\n"\
		      "4. Verify\n"\
		      "sudo docker run hello-world\n"\
                      "5. More:\n"\
                      "https://docs.docker.com/install/linux/docker-ce/fedora/#install-docker-ce-1\n"\

	else:
		print "System not supported"
     
        process = Popen(['docker', '-v'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print stdout

def How2Uninstall():
	version = platform.version()
	if "Ubuntu" in version:
		print "Uninstall docker/deocker-engine on Ubuntu, following:"
		print "sudo apt-get remove docker docker-engine docker.io"	
	if "Fedora" in version:
		print "Uninstall docker/docker-engine on Fedora, following:"
		print "sudo dnf remove "\
		      "docker docker-client docker-client-latest"\
		      "docker-common docker-latest docker-latest-logroatate "\
		      "docker-logrotate docker-selinux docker-engine-selinux "\
                      "docker-engine"
def InstallSSServer():
	print "Installing SS Server."

def InstallSSCLI():
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
def main():
	#Check Docker on local machine
	process = Popen(['docker', '-v'], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	if process.returncode != SHELL_COMMAND_SUCCESS_CODE:
		print "No Docker installed"
		How2Install()
		return "[Continue to install Doker.]"
	else:
		print "Exsiting: " + stdout
		if raw_input("Want to uninstall old docker docker-engine and install docker-ce? [y/n]") in ['y', 'Y', 'yes', 'Yes', 'YES']:
			How2Uninstall()
			return "[Continue to uninstall current docker.]"
		else:
			print "Continue to install SS service based on current docker version..."
		

	#Choose to install SS CLI or Server Docker image.
	print "Want to install shadowsocks CLI or Server?"
	if raw_input("Enter 'c' for CLI, otherwise for Server: ") == 'c':
		InstallSSCLI()
	else:
		InstallSSServer()

if __name__ == "__main__":
	main()
