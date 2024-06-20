
        Build docker image : sudo docker build . -t api_analytics
        
        Run container : sudo docker run -v /data/stock:/code/data --network=postgress_api-network  --name api_analyticsContainer api_analytics 
        
        Checking docker logs : sudo docker logs api_analyticsContainer
