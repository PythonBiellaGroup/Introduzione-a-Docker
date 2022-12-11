# Mostra le info su docker
docker system info

# Mostra le reti
docker network ls
# Mostra i volumi
docker volume ls
# Lista i container
docker container ls
# Mostra i dettagli del container
docker inspect

# Esegue un container in modalità interattiva
docker run -it ubuntu /bin/bash
# Come sopra ma espone una porta e configura le variabili d'ambiente
docker run -it -p 25000:80 -e X=abc -e Y=123 centos /bin/bash 


# Salva l'id del container pbg_bedb
mysql_container_id=$(docker container ls | egrep -e 'pbg_bedb' |cut -f1 -d' ')

# Copia i file nel container
docker cp create_table.sql $mysql_container_id:/
docker cp load_data_into_db.sh $mysql_container_id:/

docker exec $mysql_container_id "chmod 700 /load_data_into_db.sh"
docker exec $mysql_container_id /load_data_into_db.sh

sudo cp daemon.json /etc/docker/daemon.json 

~/code/scripts/demo_1/mysql_with_data$ sudo docker build -t localhost:25000/mysql_with_data:0.0.3 .
