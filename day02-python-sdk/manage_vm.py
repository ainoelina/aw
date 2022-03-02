from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
import os

subscription_id = os.environ["SUBSCRIPTION_ID"]
credential = AzureCliCredential()

network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

RG_NAME = 'aino-test-rg'
LOCATION = 'westeurope'
IP_NAME = 'aino-python-ip'
IP_CONFIG = 'aino-python-ip-config'
NIC_NAME = 'aino-python-nic'

def create_vnet(name):
    vnet_creation = network_client.virtual_networks.begin_create_or_update(
        RG_NAME, name,
        {
            'location': LOCATION,
            'address_space': {
                'address_prefixes': ['10.20.0.0/16']
            }
        }
    )
    vnet_creation.wait()
    vnet_info = vnet_creation.result()
    print(f"Provisioned virtual network {vnet_info.name} with address prefixes {vnet_info.address_space.address_prefixes}")

def create_subnet(vnet, subnet, cidr):
    subnet_creation = network_client.subnets.begin_create_or_update(
        RG_NAME, vnet, subnet,
        {'address_prefix': cidr}
    )
    subnet_info = subnet_creation.result()
    print(f"Provisioned virtual subnet {subnet_info.name} with address prefixes {subnet_info.address_prefix}")
    return subnet_info.id

def provision_ip(ip_name):
    ip_provision = network_client.public_ip_addresses.begin_create_or_update(
        RG_NAME, ip_name,
        {
            "location": LOCATION,
            "sku": {"name": "Standard"},
            "public_ip_allocation_method": "Static",
            "public_ip_address_version": "IPV4"
        }
    )
    ip_result = ip_provision.result()
    print(f"Provisioned public IP address {ip_result.name} with address {ip_result.ip_address}")
    return ip_result.id

def create_nic(name, subnet, subnet_id, ip_id):
    nic_creation = network_client.network_interfaces.begin_create_or_update(
        RG_NAME, name,
        {
            "location": LOCATION,
            "ip_configurations": [{
                "name": IP_CONFIG,
                "subnet": {"id": subnet_id},
                "public_ip_address": {"id": ip_id}
            }]
        }
    )
    nic_result = nic_creation.result()
    print(f"Provisioned network interface client {nic_result.name}")
    return nic_result.id

def provision_vm(name, nic_id):
    un = 'aino'
    pw = 'Testausta1!'
    print(f"Provisioning virtual machine {name}; this operation might take a few minutes.")
    vm_creation = compute_client.virtual_machines.begin_create_or_update(
        RG_NAME, name,
        {
            "location": LOCATION,
            "storage_profile": {
                "image_reference": {
                    "publisher": 'Canonical',
                    "offer": "UbuntuServer",
                    "sku": "16.04.0-LTS",
                    "version": "latest"
                }
            },
            "hardware_profile": {
                "vm_size": "Standard_DS1_v2"
            },
            "os_profile": {
                "computer_name": name,
                "admin_username": un,
                "admin_password": pw
            },
            "network_profile": {
                "network_interfaces": [{
                    "id": nic_id,
                }]
            }        
        }
    )
    vm_result = vm_creation.result()
    print(f"Provisioned virtual machine {vm_result.name}")

def list_vms():
    vm_list = compute_client.virtual_machines.list(RG_NAME)
    status = compute_client.virtual_machines.instance_view(RG_NAME, 'aino-vm').statuses

    column_width = 40
    print("Virtual machines".ljust(column_width) + "Location")
    print("-" * (column_width * 2))
    
    for item in list(vm_list):
        print(f"{item.name:<{column_width}}{item.location}")

def stop_vm(name):
    compute_client.virtual_machines.begin_deallocate(RG_NAME, name)
    print(f"Stopped virtual machine [{name}].\n")

def start_vm(name):
    compute_client.virtual_machines.begin_start(RG_NAME, name)
    print(f"Starting virtual machine [{name}].\n")

def main():
    vnet = 'aino-python-vnet'
    subnet = 'aino-python-subnet'
    vm_name = 'aino-vm'
    # create_vnet(vnet)
    # subnet_id = create_subnet(vnet, subnet, '10.20.1.0/24')
    # ip_id = provision_ip(IP_NAME)
    # nic_id = create_nic(NIC_NAME, subnet, subnet_id, ip_id)
    # provision_vm(vm_name, nic_id)
    stop_vm(vm_name)
    start_vm(vm_name)
#    list_vms()


main()
