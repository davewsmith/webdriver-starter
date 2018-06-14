# vi: set ft=ruby :

$provision = <<SCRIPT
sudo apt-get update

sudo apt-get install -y python-virtualenv

sudo apt-get install -y xvfb
sudo apt-get install -y firefox
sudo apt-get install -y chromium-chromedriver

# Get geckodriver from Mozilla
(
    mkdir /tmp/geckodriver
    cd /tmp/geckodriver
    wget -q https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
    tar xvfz geckodriver-v0.20.1-linux64.tar.gz
    # Put geckodriver where $PATH already points. Alternatively, you could put
    # it elsewhere and change your $PATH
    sudo mv geckodriver /usr/local/bin/
)

# Since we're in a VM, move to the shared directory.
# If you're consulting this for setting up webdriver
# outside of a VM, ignore this.
cd /vagrant

virtualenv venv --python=python3
# venv/bin/pip is 1.5.4
venv/bin/pip install --upgrade pip
# venv/bin/pip is pip now 10.0.1, which copes a lot better

venv/bin/pip install -r requirements.txt

SCRIPT


Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"

    config.vm.provider "virtualbox" do |vb|
        vb.name = "Webdriver Example"
        vb.memory = 2048
        vb.cpus = 1
    end

    config.vm.provision :shell, inline: $provision, privileged: false
end
