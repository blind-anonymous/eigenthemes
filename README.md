# Eigenthemes
Source code for "Low-rank Subspaces for Entity Linking without Annotated Data"

## Important Note
There is a minor inconsitency in the notation used for denoting the number of components of the learned subspace in the paper. Both the symbol *'n'* and *'k'* have been used in different parts of the paper for denoting the number of components. We respectfully request the reviewers to kindly ignore this minor error. Furthermore, we feel it should be quite clear to the reader given the context.

## Detailed instructions to run the code
1. Clone this repository using `git clone https://github.com/blind-anonymous/eigenthemes.git`
2. Download [Anaconda](https://www.anaconda.com/distribution/#download-section) (64-bit Python 3.7 version)
3. Setup the virtual environment named `el` to install all the required dependencies
	`conda env create -f el.yml`
4. Activate the installed environment
	`conda activate el`
5. Download the *resources* (`data` and `embeddings`) available via [google drive](https://drive.google.com/drive/folders/1iRxfWpE9AabIoO5gFHpqIrFhAyPQ6IRq?usp=sharing) (no sign-in required)
    1. Unzip the *data.zip* file in the empty `data` directory provided with the code repository
    2. Unzip the *deepwalk_wikidata.pickle.zip* file in the empty `embeddings` directory provided with the code repository
6. **Reproducing results presented in Table-3**
    * **NameMatch Baseline**: Run `python baselines_table3.py`. This script will produce the results for the name-matching baseline as described in the paper for each of the four datasets considered in this study.
    * **Other Techniques**: Run `python unsupervised_el.py`. This script will produce the results for five techniques, namely (1) Avg, (2) Eigen, (3) WAvg, (4) Degree, and (5) WEigen for all the four considered datasets. The descriptions of the techniques can be found in the paper.
    * The overall micro *Precision@1* and *MRR* is present in the 12th and 13th column of the results files. Additional information can be self-inferred, thanks to the descriptive header present in each output file.
    *Note: The results are stored in the empty directory `results` provided with the code repository. Precomputed results for the aforementioned five techniques for all the datasets have already been updated in `results` directory of the code repository. Also, the results filenames are self-explanatory.*
7. **Reproducing results presented in Table-2**
	* Run `python baselines_le_titov_table2.py` to obtain the results reported in the Table-2 of the paper.