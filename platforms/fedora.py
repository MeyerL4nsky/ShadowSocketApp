class Fedora:
	name = None

	def __init__(self, name):
		self.name = name
	def InstallDockerCE(self):
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

	def UninstallDockerCE(self):
		print "Uninstall docker/docker-engine on Fedora, following:"
		print "sudo dnf remove "\
		      "docker docker-client docker-client-latest"\
		      "docker-common docker-latest docker-latest-logroatate "\
		      "docker-logrotate docker-selinux docker-engine-selinux "\
                      "docker-engine"
