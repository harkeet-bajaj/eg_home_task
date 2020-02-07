# EG_Home_Task
 Provisioning of Kafka and Prometheus using vagrant

TASK DESCRIPTION

	Use Vagrant, Ansible to provision 3 VMs (Centos7)
	Install and configure Kafka on VM1 (with Ansible)
	Create topics on Kafka 'input', 'output'
	Create solution 1 that produces epoch timestamp in ms to 'input' once per second
	Create solution 2 that consumes from topic 1, transforms input message to date string (RFC 3339), sends to topic 'output'
	Deploy both solutions to VM2. They should both be managed as systems services.
	In VM3 install Prometheus, Grafana. Find a way to export Kafka metrics and metric from solutions 1,2 and visualize them in Grafana.
 
notes:
	everything (OS, Kafka all necessary packages for applications and applications) must be installed/provisioned automatically using Vagrant/Ansible
	documentation must be provided (how to connect to VMs, access metrics)


PROVISIONING THE ENVIRONEMENT

Clone or download the pubic GitHub repository to obtain the vagrantfile and the necessary ansible roles to provision the environment.

Dependencies for provisioning the environment:
	Vagrant 
	VirtualBox
Note: Code is not dependent on local installation of ansible engine on the host machine as vagrant file is using the Ansible Local provisioner allowing us to provision the guest using Ansible playbooks by executing ansible-playbook directly on the guest machine.


1.	Clone the git repo or download the repository zip from the gihub to local machine.

2.	Change directory to the eg_home_task folder.

3.	Provision the vagrant environment using the following vagrant command
		vagrant up
