#!/bin/sh
#SBATCH --partition=3080ti
#SBATCH --job-name=deeplearning
#SBATCH --nodes=1		# Number of nodes
#SBATCH --ntasks-per-node=1	# processes per node: 4;  Note: if gpus-per-task=1, ntasks-per-node==gres=gpu:
#SBATCH --gres=gpu:1		# Number of GPUs: 4
#SBATCH --gpus-per-task=1	# Number of GPUs per process

module load intel/2020

# Suboption 1. My conda: fail to call conda 
#  source /data/home/liuhanyu/anaconda3/etc/profile.d/conda.sh
#  module load cuda/11.6
#  conda activate workdir

# Suboption 2. /share/app/anaconda3: 
source /share/app/anaconda3/etc/profile.d/conda.sh
module load cuda/11.3
conda activate mlff

mpirun -np $SLURM_NPROCS python test.py > output 
