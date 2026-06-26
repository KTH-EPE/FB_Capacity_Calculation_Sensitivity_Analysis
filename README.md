# Sensitivity Analysis of Flow-Based Capacity Calculation

Master thesis project: Sensitivity analysis on Flow-Based Capacity calculation
using a two-stage Morris–Sobol pipeline on the Nordic 32 test 

## Overview
This project identifies which uncertain inputs:
    - individual loads forecast, 
    - wind generation forecast, 
    - GSK strategies, 
    - and topology errors.

That influence Remaining Available Margin (RAM) and PTDF in the flow-based domain the most.

## Tools
- Python 3.x
- PyPowSyBl 
- SALib 
- NumPy, Pandas, Matplotlib

## Project Structure
- `network.py` — Nordic 32 network setup and zone adaptation
- `Simulation screened norms.ipynb` — FB capacity calculation + sensitivity analysis(Morris screening → Sobol ranking)
