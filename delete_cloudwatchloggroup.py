import boto3
from botocore.exceptions import ClientError
import argparse

client = boto3.client('logs', region_name='me-central-1')

def delete_log_group(log_group_name):
    try:
        response = client.delete_log_group(
            logGroupName=log_group_name
        )
        print(f"Log group '{log_group_name}' deleted successfully.")
        return response
    except ClientError as e:
        print(f"Error deleting log group '{log_group_name}': {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete admin and api AWS CloudWatch Log Groups.")
    parser.add_argument('base_name', type=str, help='Base name for the log groups')
    args = parser.parse_args()

    base_name = args.base_name

    log_groups_to_delete = [
        f"/ecs/{base_name}-api",  
        f"/ecs/{base_name}-admin"  
    ]
    for log_group in log_groups_to_delete:
        delete_log_group(log_group)
