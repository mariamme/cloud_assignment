# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import itertools
from azure.storage.blob import BlobServiceClient


def main(contname: str) -> list:
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=mapreducer;AccountKey=ffFDRcSJfPEKJlIKwMtb3SF1LYr80o04z8N7oSLtybi1Zqqga8OEuJcqIuI7fe9skgusmgYdb5AP+ASthvlbZA==;EndpointSuffix=core.windows.net")
    container_client = blob_service_client.get_container_client(container = contname) 
    
    bloblist = container_client.list_blobs()

    linesplusoffset = []
    
    for blob in bloblist:

        file = container_client.download_blob(blob.name).readall()
        lines = file.splitlines()
        
        pair = []
        offset = 0
        for i in lines:
            offset = offset +  1
            pair.append((offset, str(i)))
        linesplusoffset.extend(pair)
        
    return linesplusoffset
