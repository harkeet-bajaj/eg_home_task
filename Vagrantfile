# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 
  config.vm.box = "centos/7"

  config.vm.define "kafka" do |kafka|
    kafka.vm.hostname  = "kafka"
    kafka.vm.network "private_network", ip: "192.168.30.101"
  end

  config.vm.define "solutioner" do |solutioner|
    solutioner.vm.hostname  = "solutioner"
    solutioner.vm.network "private_network", ip: "192.168.30.102"
  end

  config.vm.define "prometheus" do |prometheus|
    prometheus.vm.hostname  = "prometheus"
    prometheus.vm.network "private_network", ip: "192.168.30.103"
  end

  config.vm.define 'provisioner' do |provisioner|
    provisioner.vm.hostname = "provisioner"
    provisioner.vm.network "private_network", ip: "192.168.30.111"
    provisioner.vm.synced_folder "./provision_env", "/tmp/provision_env", 
      create: true,
      type: "rsync"

    provisioner.vm.synced_folder ".vagrant", "/tmp/provision_env/.vagrant",
      create: true,
      type: "rsync"

    provisioner.vm.provision :ansible_local do |ansible|
      ansible.playbook       = "evolution.yml"
      ansible.verbose        = true
      ansible.install        = true
      ansible.limit          = "all"
      ansible.provisioning_path = "/tmp/provision_env"
      ansible.inventory_path = "/tmp/provision_env/inventory"
    end
  end  

end
