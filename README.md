# http://mediascape.club

## About 

Mediascape is a web application designed for discussing various forms of 
media such as books, movies, TV shows, and music. What differentiates Mediascape
from other platforms, like Reddit and Twitter, is that threads are not user generated.

For example, to discuss a book on Reddit, a user must either find a thread where 
the book is being discussed or create their own thread. The issue with this is that 
discussion of a certain item is scattered across multiple threads, and subject to the
algorithms that govern the visibility of threads on that platform. 

On the other hand, Mediascape has one thread for every book. This serves to consolidate
the conversation about this book to one location. Users will never have to create their 
own post and hope that it will become successful. They simply find the page correspoding 
to their book, and join the conversation. Media discussion is a significant subset of the 
use cases that larger discussion platforms serve. Mediascape strives to cater directly to this 
subset, and offer a better and more focused experience. 

## Stack

Mediascape is a containerized Django web application built with Docker/ Docker-Compose. 
It uses PostgreSQL for its database, and is served with Gunicorn and Nginx. The application
is deployed to an AWS EC2 instance with Jenkins and Ansible. Jenkins runs on a Raspberry Pi,
which is provisioned with https://github.com/nickmpaz/rpi-jenkins.


- Django
- PostgreSQL
- Jenkins
- Ansible
- Docker/ Docker-Compose
- Nginx
- Gunicorn

## CI/CD Pipeline

1. Changes are made to the application using a local development Docker-Compose environment.
2. Changes are commited and pushed to this remote repository.
3. A Jenkins multi-branch pipeline sees the changes and runs its build process.
    1. Checks out the new code.
    2. Runs unit tests.
    3. Deploys new code to EC2 instance with Ansible playbook.