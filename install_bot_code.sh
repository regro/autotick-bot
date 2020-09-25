#!/bin/bash

export START_TIME=$(date +%s)
export TIMEOUT=7200

git clone --depth=1 https://github.com/regro/cf-scripts.git

pushd cf-scripts
export GIT_FULL_HASH=$(git rev-parse HEAD)
conda create -n run_env --quiet --file requirements/run
conda activate run_env
conda info
conda config --show-sources
conda list --show-channel-urls
python setup.py develop
popd

git clone --depth=1 https://github.com/regro/cf-graph-countyfair.git cf-graph
git clone --depth=1 https://github.com/conda-forge/conda-forge-pinning-feedstock.git
