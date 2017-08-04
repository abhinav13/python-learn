#!/bin/bash

openstack role create heat_stack_owner
mkdir ~/tempest
cd ~/tempest
/usr/share/openstack-tempest-*/tools/configure-tempest-directory

os_password=''
while read line;
do
  if [[ $line == *"OS_PASSWORD"* ]]; 
  then 
    os_password=$(echo $line | cut -d'=' -f2)
  fi
done <~/r2rc

tools/config_tempest.py --create --deployer-input ~/tempest-deployerinput.conf service_available.swift False  service_available.sahara False service_available.aodh True object-storage-feature-enabled.discoverability False  network-feature-enabled.ipv6_subnet_attributes False identity.uri http://100.82.35.60:5000/v2.0 identity.admin_username admin  identity.admin_password $os_password identity.admin_tenant_name admin

