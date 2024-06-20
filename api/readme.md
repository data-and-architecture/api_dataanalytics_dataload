1. sudo docker build . -t fastapi:latest
2. 
3. sudo docker run --network=postgress_api-network -d -p 80:80 --name fastAPIContainer fastapi:latest
