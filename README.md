### Overview

Input files for idealized COAWST model runs, used to examine effects of wind, surface gravity waves and stratification on inner shelf circulation. 

These files are used as input for idealized ROMS and SWAN runs. These files are project-specific and do not contain source code for the COAWST modeling system. For more information about COAWST, visit the [COAWST home page](https://www.usgs.gov/software/coupled-ocean-atmosphere-wave-sediment-transport-coawst-modeling-system)

### Contact

Please contact T. Connolly (tconnolly@mlml.calstate.edu) if using the bottom streaming parameterizations included in this repository.

### License

All ROMS code is licensed under a MIT/X style license (see License_ROMS.txt).

### Contents

#### Project directories

Input files for model runs are located in `ProjectName/RUNS`. To implement a model run, copy contents to `ProjectName` directory. The `coawst.bash` file will need to be edited for different systems.

* `InnerShelf` - Response to wind stress in a periodic channel with varying stratification and bottom slope.
* `Shoreface_Scandura_bs` - Response to wave forcing in laboratory setting (Scandura and Foti).
* `Shoreface_event`	- Response to combined wind and wave forcing.
* `Shoreface_v31_bs` - Sensitivity to bottom streaming parameterization over idealized shoreface.
* `Shoreface_v31_swanonly` - Input files to generate wave forcing for Shoreface runs in SWAN.
* `lentz_test` - Response to wave forcing in 1D water column, sensitivity to stratification.

#### Parameterizations

* `streaming_parameterizations/set_vbc.F` - A modified version of `set_vbc.F` used to modify bottom stress in order to account for wave-induced bottom streaming. Place in `ROMS/Nonlinear` directory of COAWST source code.
