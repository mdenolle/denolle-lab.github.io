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
   pip install -e .
   ```
3. Run the tests:
   ```bash
   pytest
   ```

## License
See [LICENSE](LICENSE) for licensing details.
