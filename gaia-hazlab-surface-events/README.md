# GAIA HazLab Surface Events

This repository provides a scaffold for analyzing and documenting surface event data within the GAIA HazLab project. It includes a minimal Python package, reproducible environment configuration, and placeholders for notebooks and tests.

## Project layout
- `src/gaia_hazlab_surface/`: Python package for analysis utilities.
- `notebooks/`: Interactive notebooks for exploratory analysis.
- `tests/`: Basic testing harness for the package.

## Getting started
1. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate gaia-hazlab-surface-events
   ```
2. Install the package in editable mode:
   ```bash
   python -m pip install -e .
   ```
3. Run the tests:
   ```bash
   pytest
   ```

## Pixi setup
Pixi provides a cross-platform environment and a `dask` app entrypoint.

1. Install the environment:
   ```bash
   pixi install
   ```
2. Install the package in editable mode:
   ```bash
   pixi run python -m pip install -e .
   ```
3. Run the Dask app:
   ```bash
   pixi run dask --help
   ```

## License
See [LICENSE](LICENSE) for licensing details.
