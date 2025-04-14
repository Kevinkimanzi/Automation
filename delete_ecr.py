import argparse
import boto3
from botocore.exceptions import ClientError
ecr_client = boto3.client('ecr', region_name='me-central-1')

def delete_repo(repo_name):
    try:
        response = ecr_client.delete_repository(
            repositoryName=repo_name,
            force=True  
        )
        print(f"Repository '{repo_name}' and all images deleted successfully.")
        return response
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None
def main():
    parser = argparse.ArgumentParser(description='Delete an Amazon ECR repository and all images inside it.')
    parser.add_argument('repo_name', type=str, help='The name of the ECR repository to delete along with all images inside it')
    args = parser.parse_args()
    delete_repo(args.repo_name)
if __name__ == "__main__":
    main()
