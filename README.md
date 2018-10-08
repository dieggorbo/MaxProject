# MaxProject Description
[STACK] - Graylog/MongoDB CLuster/Python app(Flask)

This project deploy an application Stack containing a simple form using python Flask framework that save this info into a MongoDB collection. As a plus, a Graylog stack is also deployed to handle logs


# REQUIREMENTS
Necessary to change the sysctl parameter vm.max_map_count before clone this repo.Run the below line to do this 

 echo 'vm.max_map_count=262144' >> /etc/sysctl.conf && sysctl -a && sysctl -p

# INSTALLATION
~$ git clone https://github.com/dieggorbo/MaxProject.git
~$ cd MaxProject
~$ docker-compose up

# ACCESSING RESOURCES
 - Graylog
   URL: http://<IP>:9000
   USER: admin
   PWD: admin

 - Application
   URL: https://<IP>

 
# TODO
 - Implement NGINX cache layer to handle SSL/HTTP2 connections,redirect HTTP to HTTPS and also speed up content delivery with some cache rules
 - Implement mongodb HA cluster since AWS t2.micro instance could not deal with the app load  =[
 - Beautify frontend
