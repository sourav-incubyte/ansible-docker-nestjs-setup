#!/bin/bash

set -e

echo "Checking and installing required dependencies..."

# Ensure Python and pip are installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python..."
    apt-get update
    apt-get install -y python3 python3-pip
fi

# Ensure curl is installed
if ! command -v curl &> /dev/null; then
    echo "Installing curl..."
    apt-get update
    apt-get install -y curl
fi

echo "Installing Ansible..."
pip3 install ansible

echo "Installing Node.js..."
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get install -y nodejs

echo "Copying NestJS application..."
cp -r /solution/nestapp /app/nestapp

echo "Installing NestJS dependencies..."
cd /app/nestapp && npm install

echo "Building NestJS application..."
cd /app/nestapp && npm run build

echo "Running Ansible playbook to set up infrastructure..."
cd /app && ansible-playbook /solution/playbook.yml

echo "Done!"
