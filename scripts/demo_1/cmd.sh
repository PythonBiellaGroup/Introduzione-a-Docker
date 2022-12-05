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

mysql_container_id=$(docker container ls | egrep -e 'pbg_bedb' |cut -f1 -d' ')

docker cp create_table.sql $mysql_container_id:/
docker cp load_data_into_db.sh $mysql_container_id:/
