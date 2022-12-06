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
       sudo apt-get update; sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
