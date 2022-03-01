from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os


subscription_id = os.environ["SUBSCRIPTION_ID"]
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

def list_rg():
    group_list = resource_client.resource_groups.list()
    
    column_width = 40
    print("Resource Group".ljust(column_width) + "Location")
    print("-" * (column_width * 2))
    
    for group in list(group_list):
        print(f"{group.name:<{column_width}}{group.location}")

def create_rg(rg_name):
    resource_client.resource_groups.create_or_update(rg_name, {"location": "westeurope"})

def get_rg(rg_name):
    print(f"Resource group with name [{rg_name}] exists: ", end="")
    print(resource_client.resource_groups.check_existence(rg_name))

def update_rg(tag, value):
    rg_name = "aino-test-rg"
    rg_params = {'location':'westeurope'}
    rg_params.update(tags={tag:value})
    resource_client.resource_groups.create_or_update(rg_name, rg_params)

def delete_rg(rg_name):
    delete_rg = resource_client.resource_groups.begin_delete(rg_name)
    delete_rg.wait()

def main():
    create_rg("aino-test-rg")
#    list_rg()
    get_rg("aino-test-rg")
    update_rg("tag2", "value2")
    delete_rg("aino-test-rg")

main()