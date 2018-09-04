import yaml

repos = {"FIRST":{"ID":"TEST4","USER":"mwolotsky"}}
with open("repos.yaml",'w') as f:
    yaml.dump(repos,f)
