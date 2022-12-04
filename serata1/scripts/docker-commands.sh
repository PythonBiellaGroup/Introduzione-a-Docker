# Manual remove all containers pending
docker rm $(docker ps -a -q)