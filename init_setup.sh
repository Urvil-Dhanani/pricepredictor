echo [$(date)]: "starting init_setup.sh"
echo [$(date)]: "creating environment with python v3.8"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "activating the environment"

conda activate ./env

echo [$(date)]: "installing the development requirements"

pip install -r requirements_dev.txt

echo [$(date)]: "init_setup.sh has been executed successfully"