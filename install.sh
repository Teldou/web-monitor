#!/bin/bash

curl https://pyenv.run | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 3.10.1
pyenv global 3.10.1

sudo apt update
sudo apt install redis-server

pip install -r Server/requirements.txt
pip install -r Telegram/requirements.txt