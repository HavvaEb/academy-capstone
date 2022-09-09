import boto3
import json
import logging
def get_snowflake_creds_from_sm(secret_name: str):
    sess = boto3.Session(region_name="eu-west-1")
    client = sess.client('secretsmanager')

    response = client.get_secret_value(
        SecretId=secret_name
    )
    
    creds = json.loads(response['SecretString'])
    return {
        "sfURL": f"{creds['URL']}",
        "sfPassword": creds["PASSWORD"],
        "sfUser": creds["USER_NAME"],
        "sfDatabase": creds["DATABASE"],
        "sfWarehouse": creds["WAREHOUSE"],
        "sfRole": creds["ROLE"],
            "sfSchema": "HAVVA_EBRAHIMIPOUR",
            "dbtable": "CAPSTONE"
            
        }
        

def write_df_with_options(df, format: str, mode: str, options: dict):
    df.write.format(format).options(**options).mode(mode).save()