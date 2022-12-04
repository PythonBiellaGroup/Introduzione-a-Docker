# Intall docker (manual common guide): not working in ubuntu 20.04 server
# 1- Remove packages if present:
	sudo apt-get remove docker docker-engine docker.io containerd runc
# 2- Update packages
	sudo apt-get update
# 3- Install pre-requisites
	sudo apt-get install ca-certificates curl gnupg lsb-release
# 4- Add GPG keys
	sudo mkdir -p /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# 5- Add repo
	echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# 6- Install
	sudo apt-get update; sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-compose

### Ubuntu instructions (for docker and swarm)
# 1. update
sudo apt update
# 2. install requirements
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
# 3. install docker repository signing key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 4 add docker repository
sudo add-apt-repository "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# 5 update packages
sudo apt update
# 6 install docker
sudo apt install docker-ce -y
# 7 install other tools
sudo apt install docker-compose docker-ce-cli containerd.io -y
# 8 check docker status
sudo systemctl status docker
# 9 enable docker start automatically
sudo systemctl enable docker
# 10 add current user to group docker (to avoid sudo)
sudo usermod -aG docker ${USER}

## If you have errors, remove (on Ubuntu):
sudo rm /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list 
sudo rm /etc/apt/sources.list.d/docker.list 

# Create docker swarm cluster
# To create a Docker Swarm cluster, you will first need to initialize the swarm mode on the manager node. 
# Then, join the worker nodes to the cluster. Strictly use the nodes IP address.
# 1. Initialize swarm
sudo docker swarm init --advertise-addr 192.0.2.11
# Go to the worker-1 node and add it to the cluster. Modify the --token value with your own.
# You can generate and encode a token to be more secure
sudo docker swarm join --token SWMTKN-1-2jxta71638d1pyioznb9jo4hi4u5ppd8t7lc90linwi9acu54s-aef4mqdy23ktrkcxsp57uyoma 192.0.2.11:2377
# Go to the manager node and verify if all the worker nodes successfully joined the cluster.
sudo docker node ls


# Example deploy on cluster
# Go to the manager node and create a 'Docker getting started web-page' service named docker-tutorial that will run on default http port 80 and expose it to port 80 on the host server.
sudo docker service create --name docker-tutorial --publish 80:80 docker/getting-started
# verify status of the service
sudo docker service ls
# create a replica
sudo docker service scale docker-tutorial=2
# verify status of the replica
sudo docker service ls
# from the browser access to the service from all your node
# manager node: http://192.0.2.11
# worker node: http://192.0.2.12


