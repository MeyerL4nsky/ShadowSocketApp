class Ubuntu:
	name=None

	def __init__(self, name):
		self.name = name

	def InstallDockerCE(self):
		print "Install Docker on {PlatformName}, following:".format(PlatformName = self.name)
                print "1. Set up docker repository:"\
                      "  sudo apt-get update\n"\
                      "  sudo apt-get install apt-transport-https ca-certificates curl software-properties-common\n"\
                      "  curl -fsSL http://download.docker.com/linux/ubuntu/gpg | sudo apt=key add -\n"\
                      "  sudo apt-key fingerprint 0EBFCD88\n"\
                      "  sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) satble'\n"\
                      "2. Install Docker form repo:\n"\
                      "  sudo apt-get update\n"\
                      "  sudp apt-get install docker-ce\n"\
                      "3. Start Docker:\n"\
                      " Auto Run on {PlatformName}\n"\
                      "4. Verify:\n"\
                      " sudo docker run hello-world\n"\
                      "5. More:\n"\
                      "https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1\n".format(PlatformName = self.name)
	
	def UnistallDockerCE(self):
		print "Uninstall docker/docker-engine on {PlatformName}, following:".format(PlatforName = self.name)
                print "sudo apt-get remove docker docker-engine docker.io"

