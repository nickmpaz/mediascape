#!/bin/sh

ssh -i ~/myAmazonKey.pem ubuntu@ec2-3-135-208-246.us-east-2.compute.amazonaws.com << EOF
    cd mediascape
    ls
    # docker-compose down
    # git pull
    # docker-compose -f docker-compose.prod.yml up -d --build
EOF