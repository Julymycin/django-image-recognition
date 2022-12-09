#!/bin/bash

# Download the Miniconda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install Miniconda
bash Miniconda3-latest-Linux-x86_64.sh

source ~/.bashrc

# Create a new conda environment named "my_env" with Python 3.7
conda create -n cs django

# Activate the conda environment
conda activate cs

# Install the "djangorestframework" and "pytorch" packages in the environment
conda install -c conda-forge djangorestframework
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# run the server
nohup python manage.py runserver 0.0.0.0:8000 &