# 1 Traditional way

### Create a virtual environment

```
python -m venv <venv_name>
-m : module flag to run library modules as scripts
```


to create a virtual environment with the specified version of Python

```
 python3.12 -m venv <venv_name>
```

### Activate the virtual environment

```
<venv_name>\Scripts\activate
```

### Install a packages from requirements.txt

```
pip install -r requirements.txt
```

# 2 Using uv

### Create a virtual environment

```cmd
uv venv --python 3.12
uv venv --activate

uv pip install -r requirements.txt
uv run <script_name>.py

# Creates a project with a virtual environment and a main script

uv init project_name 
uv pip install -r requirements.txt

uv add <package_name>
uv run <script_name>.py

```

# 3 Using Conda

### Create a virtual environment

```conda create --name <env_name> python=3.12</code>
``` 
to create a virtual environment with the specified version of Python
### Activate the virtual environment

```
conda activate <env_name>
```
### Install a packages from requirements.txt

```
pip install -r requirements.txt
```
