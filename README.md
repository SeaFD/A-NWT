# A-NWT: Axisymmetric Numerical Wave Tank

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![OpenFOAM](https://img.shields.io/badge/OpenFOAM-Compatible-green.svg)](https://www.openfoam.com/)

## Overview

Axisymmetric numerical wave tank implemented in OpenFOAM for efficient simulation of heaving sphere dynamics. Achieves 50-100x computational speedup compared to full 3D simulations while maintaining high accuracy for axisymmetric geometries.

## Associated Publication

This case setup is described in detail in the following publication:

**Davidson, J., Nava, V., Andersen, J., & Kramer, M. B.** (2024). Exploiting Axisymmetry to Optimize CFD Simulations—Heave Motion and Wave Radiation of a Spherical Buoy. *Symmetry*, 16(9), 1252. [https://doi.org/10.3390/sym16091252](https://doi.org/10.3390/sym16091252)

**If you use this numerical wave tank in your research, please cite the above publication.**

## Features

- **Computational Efficiency**: 50-100x faster than 3D equivalents
- **High Accuracy**: Validated against physical wave tank experiments
- **Custom Mesh Generator**: Automated axisymmetric mesh tool
- **Complete Test Case**: Heaving sphere drop test included

## Quick Start

```bash
# Clone repository
git clone https://github.com/SeaFD/A-NWT.git
cd A-NWT

# Extract case and mesh maker
tar -xf ANWT_dropHeight_03D.tar.xz
tar -xf polyMeshMaker.tar.xz

# Run case
cd ANWT_dropHeight_03D
source /path/to/OpenFOAM/etc/bashrc
blockMesh
setFields
interFoam
```

## Case Description

- **Geometry**: Heaving sphere (D = 0.3 m)
- **Initial Drop Height**: 0.3D (0.09 m)
- **Validated**: Heave motion and wave radiation

## License

GNU GPL v3.0 - see [LICENSE](LICENSE)

## Author

**Josh Davidson**  
ORCID: [0000-0001-5966-4272](https://orcid.org/0000-0001-5966-4272)

## Citation

If you use this code, please cite:
```bibtex
@article{davidson2024exploiting,
  title={Exploiting Axisymmetry to Optimize CFD Simulations—Heave Motion and Wave Radiation of a Spherical Buoy},
  author={Davidson, Joshua and Nava, Vicente and Andersen, Jonas and Kramer, Morten Bech},
  journal={Symmetry},
  volume={16},
  number={9},
  pages={1252},
  year={2024},
  publisher={MDPI},
  doi={10.3390/sym16091252}
}
```

## Related

- [NWT_potentialFreeSurfaceFoam](https://github.com/SeaFD/NWT_potentialFreeSurfaceFoam)
- [potentialFreeSurfaceFoam](https://github.com/SeaFD/potentialFreeSurfaceFoam)
