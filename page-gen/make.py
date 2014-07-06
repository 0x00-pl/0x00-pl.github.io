import os

current_cwd= os.getcwd()
root_cwd= os.path.split(current_cwd)[0]
web_site_cwd= os.path.join(root_cwd,'web-site')


import index

index.gen(web_site_cwd)
