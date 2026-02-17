To run the variant calling benchmark:

1. Install conda environment `evaluation_VC/environment.yml`
2. Fill the `evaluation_VC/experiments.json`
    1. `ROOT_OUT` - output directory
    2. `ROOT_IN` - repository directory
    3. `DATA` - directory with input reads and variants (initially empty, datasets are downloaded/simulated by the benchmark pipeline)
    4. `COMMITS` - strobealign versions used in the benchmark
3. Run `snakemake -s evaluation_VC/Snakefile --configfile evaluation_VC/experiments.json`
4. Output results are located in `ROOT_OUT/evaluation_SV`
