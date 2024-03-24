A demonstration of Docker to implement a simple 3 tier architecture

    frontend will be able to access the mid-tier
    mid-tier will be able to access the db

In order to run this in docker, simply type docker-compose up at the command prompt. Docker will then create the MongoDB from the stock mongo image. The api uses nodejs with express and is built from a node:alpine image. The front end uses ReactJS and built from a node:alpine image.
