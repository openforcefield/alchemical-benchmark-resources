# Good To Know

This page contains information that would be good to know about the specifics of running alchemical calculations for OpenFF affiliate use. The accuracy of this information is not guaranteed.

**Benchmark Salt Concentration**
- In `openfe` RBFEs are run with 0.15 M NaCl by default to correspond to experimental buffers. We don’t know exactly what the buffer concentrations are and it would be a pain to find out, but what we have is better than the 0 M that Schrodinger runs for their benchmarks.
- Note that the "concentration of salt" in a simulation can translate to a different number of ions depending on the method used to add salt. Two methods include the [SLTCAP](https://pubs.acs.org/doi/10.1021/acs.jctc.7b01254) method and the OpenMM neutralization approach (as of 2026/03).
- Chapin's Rosemary simulations use the SLTCAP approach, while OpenFE benchmarks use the OpenMM neutralization approach.

**`feflow` - Folding@Home**
`feflow` is a repository of community developed protocols, mostly Chodera Lab custom protocols right now. Note that because of the way openfe protocols are structured, we run on traditional HPC, but the Chodera Lab protocols can be run on Folding@Home.