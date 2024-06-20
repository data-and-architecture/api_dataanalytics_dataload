Build docker image : sudo docker build . -t srcapi

Run container : sudo docker run -v /data/stock:/code/data --network=postgress_api-network  --name srcAPIContainer srcapi 

Checking docker logs : sudo docker logs srcAPIContainer

Remove container :sudo docker rm srcAPIContainer

Remove images: docker rmi image name

