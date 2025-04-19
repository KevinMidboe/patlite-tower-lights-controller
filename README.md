# PATLITE light tower controller

## frontend

setup

```
cp .env.exmaple .env
```

build

```
cd frontend
yarn
yarn build

# docker build
build -t patlite-light-tower-controller .
```

## server

```
cd server
virtualenv env
source env/bin/activate

pip3 install -r requirements.txt
python3 main.py

or

python3 --server main.py
```
