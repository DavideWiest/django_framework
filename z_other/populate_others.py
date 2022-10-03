"Simple program to populate config file - execute from base directry (parent of z_other)"
from jinja2 import Template

pop_file = input("Populate .conf file or wsgi file? [c = conf ; w = wsgi]: ")
program_running = True
project_name = input("Project name: ")
project_branch_name = input(f"Project branch name [m = {project_name}-master ; m2 = {project_name}-main ; custom]: ")
project_path = input(f"Project path [a = /var/www/html/{project_name}/{project_name}-master ; b = /var/www/html/{project_name}/{project_name}-main ; custom]: ")


if project_branch_name == "m":
    project_branch_name = f"{project_name}-master"
elif project_branch_name == "m2":
    project_branch_name = f"{project_name}-main"

if project_path == "a":
    project_path = f"/var/www/html/{project_name}/{project_name}-master"
elif project_path == "b":
    project_path = f"/var/www/html/{project_name}/{project_name}-main"


pop_file_dict = {
    "c": f"config.conf",
    "w": "wsgi.py"
}

try:
    with open("z_other/" + pop_file_dict[pop_file], "r", encoding="utf-8") as f:
        template = Template(f.read())
    output = template.render(project_name=project_name, project_branch_name=project_branch_name, project_path=project_path)
    print(output)
except KeyError:
    print("wrong input. restart")