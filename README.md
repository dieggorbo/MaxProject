# MaxProject Description
[STACK] - Graylog/MongoDB CLuster/Python app(Flask)

This project deploy an application Stack containing a simple form using python Flask framework that save this info into a MongoDB collection. In a plus, a Graylog stack is also deployed to handle logs


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

 
