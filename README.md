To run the variant calling benchmark

<ol>
    <li>Install conda environment `evaluation_VC/environment.yml`</li>
    <li>Fill the `evaluation_VC/experiments.json`</li>
        <li>`ROOT_OUT` - output directory</li>
        <li>`ROOT_IN` - repository directory</li>
        <li>`DATA` - directory with input reads (initially empty, datasets are downloaded/simulated by the benchmark pipeline)</li>
        <li>`COMMITS` - strobealign versions used in the benchmark</li>
    <li>
    <li> Run `snakemake -s evaluation_VC/Snakefile --configfile evaluation_VC/experiments.json`
</ol>