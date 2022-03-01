from venv import create
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobClient
import os

subscription_id = os.environ["SUBSCRIPTION_ID"]
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)
RG_NAME1 = 'aino-test-rg'
SA_NAME1 = 'aino003'
conn_str = "DefaultEndpointsProtocol=https;AccountName=aino003;AccountKey=f/XsQf+J13YdsVY6SOZydycrzyTbhWiP9Yd2Du2KUsqVF+QWYvjQX6smQug2/5epNHNAEvo/XMT05MrjpWWvUQ==;EndpointSuffix=core.windows.net"

def create_rg(rg_name):
  resource_client.resource_groups.create_or_update(rg_name, {"location": "westeurope"})

def create_sa(sa_name):
    storage_client.storage_accounts.begin_create(
        RG_NAME1, sa_name,
        {
            "sku": {
            "name": "Standard_LRS"
          },
          "kind": "StorageV2",
          "location": "westeurope",
          "encryption": {
            "services": {
              "blob": {
                "key_type": "Account",
                "enabled": True
              }
            },
            "key_source": "Microsoft.Storage"
          },
          "tags": {
            "createdBy": "aino"
          }
        }
    ).result()

def list_accounts():
  account_list = storage_client.storage_accounts.list()

  column_width = 40
  print("Storage account".ljust(column_width) + "Location")
  print("-" * (column_width * 2))
    
  for item in list(account_list):
    print(f"{item.name:<{column_width}}{item.location}")

def create_container(name):
  blob = storage_client.blob_containers.create(RG_NAME1, SA_NAME1, name, {})
  print("Create blob container:\n{}".format(blob))
  
def upload_file(filename):
  blob = BlobClient.from_connection_string(conn_str, "ainoblob", filename)
  with open('lataa.txt', 'rb') as file:
    blob.upload_blob(file)

def download_file(filename):
  blob = BlobClient.from_connection_string(conn_str, "ainoblob", filename)
  with open('./download.txt', 'wb') as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)

def delete_file(filename):
  blob = BlobClient.from_connection_string(conn_str, "ainoblob", filename)
  try:
    blob.delete_blob()
  except:
    print(f"No blob with name [{filename}] found")

def delete_container(blobname):
  blob_container = storage_client.blob_containers.delete(RG_NAME1, SA_NAME1, blobname)
  print(f"Blob container [{blobname}] deleted.")
#  resource_client.resource_groups.begin_delete(RG_NAME1).result()

def delete_storage(name):
  storage_client.storage_accounts.delete(RG_NAME1, name)
  print(f"Storage account [{name}] deleted.")

def main():
#  list_accounts()
#  create_rg("aino-test-rg")
#  create_sa("aino003")
#  create_container("ainoblob")
#  upload_file("aino.txt")
#  download_file("aino.txt")
#  delete_file("aicxcno.txt")
#  delete_container("ainoblob")
  delete_storage(SA_NAME1)

main()