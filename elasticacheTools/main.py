import boto3
from dotenv import load_dotenv
import datetime
import json
import sys
import os
import os.path
from environs import Env
import string
import time

env = Env()
env.read_env()



def connect():
    ACCESS_KEY = env("ACCESS_KEY")
    SECRET_KEY = env("SECRET_KEY")
    REGION = env("REGION")
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION,
    )
    return session
    
def increase_replica(replicationGroup,nodesTotal):

    client = boto3.client('elasticache')
    
    response = client.increase_replica_count(
    ReplicationGroupId=replicationGroup,
    NewReplicaCount=nodesTotal,
    ApplyImmediately=True
    )
    
def decrease_replica(replicationGroup,nodesTotal):

    client = boto3.client('elasticache')
    
    response = client.decrease_replica_count(
    ReplicationGroupId=replicationGroup,
    NewReplicaCount=nodesTotal,
    ApplyImmediately=True
    )
    
    
def main():
    
    task=sys.argv[1]
    replicationGroup=sys.argv[2]
    nodesTotal=int(sys.argv[3])
    
    if task == "increase":
        increase_replica(replicationGroup,nodesTotal)
    else:
        decrease_replica(replicationGroup,nodesTotal)
    
    

    
if __name__ == "__main__":
    main()
