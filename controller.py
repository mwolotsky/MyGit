import yaml
from git import Repo
import os

repo_list = []
with open("repos.yaml",'r') as f:
    repos = yaml.load(f)
    for repo in repos.values():
        repo_list.append((repo["USER"],repo["ID"]))
for user,ID in repo_list:
    assert os.path.exists("/home/git/")
    if os.path.exists("/home/git/{0}".format(user)):
            if not os.path.exists("/home/git/{0}/{1}".format(user,ID)):
                bare_repo = Repo.init(os.path.join("/home/git/{0}".format(user),ID),bare=True)
                assert bare_repo.bare
                
        
