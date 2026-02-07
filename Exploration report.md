## Interesting Findings for Further Investigation

After exploring the Rental Registry, Crime (2024), and Kindergarten Readiness datasets, a few patterns stood out. These are not final conclusions, but possible relationships that could be studied further.

### 1. Rental Density and Crime May Be Related

One noticeable pattern was that ZIP codes with a large number of rental properties also seemed to have higher numbers of crime incidents.

This could mean that areas with more rentals experience more crime, but it could also be explained by higher population density in those ZIP codes.

---

### 2. Poverty Levels Might Be Connected to Crime and Housing Conditions

From the kindergarten readiness dataset, some ZIP codes showed higher poverty indicators. These same areas often appeared to have higher crime counts and fewer completed rental inspections.

This suggests that socioeconomic conditions may be linked to both safety and housing quality.

---

### 3. Missing Rental Inspection Data Could Hide Problem Areas

The rental registry contained many missing values, especially related to inspection dates and status. Some ZIP codes appeared to have much more missing data than others.

This could mean inspections are not happening evenly across neighborhoods, or that reporting is inconsistent.

---

## Documentation of LLM-Assisted Analysis with Validation Results

Large Language Models (ChatGPT) were used as a support tool throughout the exploratory data analysis process. The primary purpose of using the LLM was to assist with coding guidance, data preprocessing strategies, visualization ideas, and interpretation of exploratory results. The model was not used to generate any analytical outcomes directly.

### Areas Where LLM Assistance Was Used

The LLM supported the following tasks:

### 1. Code Development and Debugging

ChatGPT was used to help:

* Write initial Python code for loading and cleaning datasets using Pandas
* Handle missing values and datetime formatting
* Group data by ZIP code for aggregation
* Generate basic visualizations such as bar charts and histograms
* Suggest methods for merging datasets

All code provided by the LLM was manually reviewed and modified before execution. Outputs were produced locally in Jupyter Notebook.

### 2. Exploratory Analysis Guidance

The LLM suggested possible analytical directions, including:

* Comparing crime counts with rental property density
* Investigating relationships between poverty indicators and crime
* Checking missing inspection data by ZIP code
* Framing results as hypotheses rather than conclusions

These suggestions helped guide the exploration but did not replace human decision-making.

### 3. Interpretation Support

ChatGPT was also used to help summarize patterns observed in plots and tables and to assist in drafting written explanations. Final interpretations were made by reviewing actual dataset outputs.

---

## Validation Methods

To ensure accuracy and reliability, several validation steps were performed:

### Manual Verification of Results

* Aggregated DataFrames were printed and inspected directly.
* Missing values were calculated using `isnull().sum()` and verified manually.
* ZIP code groupings were checked for correctness.

### Visual Validation

* Histograms and bar charts were reviewed to confirm distributions and trends.
* Outliers were manually inspected to ensure they were not artifacts of preprocessing.

### Cross-Checking Assumptions

* Crime counts were examined alongside rental totals to avoid misleading interpretations.
* Findings were framed as correlations or hypotheses only, not causal claims.
* Population effects were acknowledged as potential confounding variables.

### Human Oversight

All findings were reviewed critically to prevent overgeneralization. The LLM’s outputs were treated as suggestions rather than authoritative conclusions. Every analytical decision was made by the user after reviewing the actual data.

---

## Validation Results

The validation process confirmed that:

* Dataset merges by ZIP code were successful and consistent.
* Missing values were accurately identified.
* Visualizations matched summary statistics.
* Observed patterns (such as rental density aligning with higher crime counts in some ZIP codes) were supported by actual computed values.

However, no statistical modeling was performed at this stage, so results remain exploratory.

---

## Summary

GPT functioned as a productivity and guidance tool rather than an analytical engine. All calculations, plots, and conclusions were generated through direct coding and verified manually. The LLM helped accelerate development but did not replace traditional data analysis methods.

