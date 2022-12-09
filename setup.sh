#!/bin/bash

# Download the Miniconda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install Miniconda
bash Miniconda3-latest-Linux-x86_64.sh

# Create a new conda environment named "my_env" with Python 3.7
conda create -n cs655 django

# Activate the conda environment
conda activate cs655

# Install the "djangorestframework" and "pytorch" packages in the environment
conda install -c conda-forge djangorestframework
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# run the server
python manage.py runserver 0.0.0.0:8000