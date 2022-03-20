# import requests
from github import Github

# import pprint
import os
import sys
import hvac

try:
    secret_path = os.environ["SECRET_PATH"]
    secret_key = os.environ["SECRET_KEY"]
except KeyError:
    print("Github Token path and key are not set")
    sys.exit(1)

vault_client = hvac.Client()
gh_token = vault_client.secrets.kv.v2.read_secret_version(
    mount_point="kv",
    path=secret_path,
)["data"]["data"][secret_key]

g = Github(gh_token)
for repo in g.get_user().get_repos():
    print(repo.name)
