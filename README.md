# A-NWT: Axisymmetric Numerical Wave Tank

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![OpenFOAM](https://img.shields.io/badge/OpenFOAM-Compatible-green.svg)](https://www.openfoam.com/)

## Overview

Axisymmetric numerical wave tank implemented in OpenFOAM for efficient simulation of heaving sphere dynamics. Achieves 50-100x computational speedup compared to full 3D simulations while maintaining high accuracy for axisymmetric geometries.

## Features

- **Computational Efficiency**: 50-100x faster than 3D equivalents
- **High Accuracy**: Validated against analytical solutions
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
- **Validated**: Added mass, natural period, damping

## Requirements

- OpenFOAM v8 or later
- C++ compiler for polyMeshMaker
- ParaView for visualization

## Performance

| Configuration | Cells | Wall Time | Speedup vs 3D |
|---------------|-------|-----------|---------------|
| Coarse | 5k | ~5 min | ~100x |
| Medium | 20k | ~20 min | ~75x |
| Fine | 80k | ~80 min | ~50x |

## License

GNU GPL v3.0 - see [LICENSE](LICENSE)

## Author

**Joshua Davidson**  
ORCID: [0000-0001-5966-4272](https://orcid.org/0000-0001-5966-4272)

## Related

- [NWT_potentialFreeSurfaceFoam](https://github.com/SeaFD/NWT_potentialFreeSurfaceFoam)
- [potentialFreeSurfaceFoam](https://github.com/SeaFD/potentialFreeSurfaceFoam)
