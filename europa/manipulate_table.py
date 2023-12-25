import os
import logging
from datetime import datetime
import aiohttp
import json

import azure.functions as func
from azure.keyvault.secrets import SecretClient
from azure.identity import ManagedIdentityCredential
from azure.storage.filedatalake import DataLakeServiceClient

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import pandas as pd

def manipulate_table(storage_account_name, storage_account_key, table_name, operation, entity=None):
    table_service = TableService(account_name=storage_account_name, account_key=storage_account_key)
    print(table_service)
    if operation == "read":
        entities = table_service.query_entities(table_name)
        data = []
        for entity in entities:
            data.append(entity)

        df = pd.DataFrame(data)
        return(df)
    elif operation == "write":
        table_service.insert_entity(table_name, entity)
        print("Entity inserted successfully.")

    elif operation == "update":
        table_service.update_entity(table_name, entity)
        print("Entity updated successfully.")

    else:
        print("Invalid operation.")



test1 = {
    'PartitionKey': 'coloré',
    'RowKey': 'brand2',
    'text': 'Marker2',
    'color': 'Purple2',
    'price': '52'
}

#result =manipulate_table("stodsalesforcemag000",
#                 "",
#                 "test",
#                 "read",test1)

# print(result)
