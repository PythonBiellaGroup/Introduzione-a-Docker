docker node ls --format '{{.ID}}' | xargs docker node inspect --format '{{.Status.Addr}}' | while read node; do

  echo "Processing node $node"

  ssh -n $node "docker ps -a --filter 'is-task=true' --format '{{.ID}} {{.Label \"com.docker.stack.namespace\"}}'" | while read container; do
    
    id=$(echo $container | cut -d ' ' -f1)
    stack=$(echo $container | cut -d ' ' -f2)
    
    found=$(docker stack ls | grep $stack | wc -l)
    
    if [ $found == "0" ]; then
        echo "no stack $stack found for container $id"
        ssh -n $node "docker rm -f $id"
    else
        echo "found stack $stack for container $id"
    fi

  done
done