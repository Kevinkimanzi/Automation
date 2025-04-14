import git
import os
# Constants
NEW_REPO = ''  # new repo to push the codebase
CLONE_REPO_URL = ''  # clone existing repo
BRANCH_NAME = 'Staging'
CLONE_DIR = '/Users/user/Kevin/clone'  # Change dir to your desired

def clone_and_checkout_branch(repo_url, branch_name, clone_dir):
    if os.path.exists(clone_dir):
        os.system(f'rm -rf {clone_dir}')  
    
    repo = git.Repo.clone_from(repo_url, clone_dir)
    repo.git.checkout(branch_name)
    print(f'Checked out branch {branch_name} from {repo_url}')
    return clone_dir

def push_to_new_repo(clone_dir, new_repo_url):
    repo = git.Repo(clone_dir)
    origin = repo.create_remote('new_origin', new_repo_url)
    origin.push(refspec=f'{repo.active_branch.name}:{repo.active_branch.name}')
    print(f'Branch {repo.active_branch.name} pushed to {new_repo_url}')

def main():
    clone_dir = clone_and_checkout_branch(CLONE_REPO_URL, BRANCH_NAME, CLONE_DIR)
    push_to_new_repo(clone_dir, NEW_REPO)
if __name__ == "__main__":
    main()