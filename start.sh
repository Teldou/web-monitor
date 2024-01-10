#!/bin/bash

read -p "Enter TELEGRAM_API_ID: " telegram_api_id
read -p "Enter TELEGRAM_API_HASH: " telegram_api_hash
read -p "Enter MONGODB_URI: " mongodb_uri
read -p "Enter BIND_ADDRESS: " bind_address
read -p "Enter REDIS_URL: " redis_url

echo "export TELEGRAM_API_ID=$telegram_api_id" >> ~/.bashrc
echo "export TELEGRAM_API_HASH=$telegram_api_hash" >> ~/.bashrc
echo "export MONGODB_URI=$mongodb_uri" >> ~/.bashrc
echo "export BIND_ADDRESS=$bind_address" >> ~/.bashrc
echo "export REDIS_URL=$redis_url" >> ~/.bashrc

screen -S redis -dm bash -c 'redis-server'
screen -S server -dm bash -c 'python3 Server/app.py'
screen -S telegram -dm bash -c 'python3 Telegram/main.py'