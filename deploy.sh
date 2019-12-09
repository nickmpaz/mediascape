#!/bin/sh

ssh -i /var/lib/jenkins/.ssh/myAmazonKey.pem ubuntu@ec2-3-135-208-246.us-east-2.compute.amazonaws.com << EOF
    cd mediascape
    docker-compose down
    git pull
    docker-compose -f docker-compose.prod.yml up -d --build
EOF