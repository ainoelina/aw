
from azure.mgmt.network import NetworkManagementClient
from azure.identity import AzureCliCredential
import os

subscription_id = os.environ["SUBSCRIPTION_ID"]
credential = AzureCliCredential()
RG_NAME = 'aino-test-rg'
VNET_NAME = 'aino-python-vnet'
LOCATION = 'westeurope'
SUBNET_NAME = 'aino-python-snet'

network_client = NetworkManagementClient(credential, subscription_id)

def list_vnets():
    network_list = network_client.virtual_networks.list(RG_NAME)

    column_width = 40
    print("Virtual network".ljust(column_width) + "Location")
    print("-" * (column_width * 2))
        
    for item in list(network_list):
        print(f"{item.name:<{column_width}}{item.location}")

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

def create_subnet(vnet, subnet, cidr):
    subnet_creation = network_client.subnets.begin_create_or_update(
        RG_NAME, vnet, subnet,
        {'address_prefix': cidr}
    )
    subnet_info = subnet_creation.result()

def delete_subnet(subnet):
    sn = network_client.subnets.begin_delete(RG_NAME, VNET_NAME, subnet)
    print(f"Subnet [{subnet}] deleted.")

def delete_vnet(vnet):
    vn = network_client.virtual_networks.begin_delete(RG_NAME, vnet)
    print(f"Vnet [{vnet}] deleted.")

def main():
#    create_vnet(VNET_NAME)
#    create_subnet(VNET_NAME, SUBNET_NAME, '10.20.1.0/24')
#    delete_subnet(SUBNET_NAME)
#    delete_vnet(VNET_NAME)
    list_vnets()

main()