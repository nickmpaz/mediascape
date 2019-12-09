#!/bin/sh
whoami
# ssh -i ~/secrets/myAmazonKey.pem ubuntu@ec2-3-135-208-246.us-east-2.compute.amazonaws.com << EOF
#     whoami
# EOF