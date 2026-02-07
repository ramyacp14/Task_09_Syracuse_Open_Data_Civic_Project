# Syracuse Open Data Civic Project Proposal

## Project Title

**Are We Inspecting Where It Matters? Evaluating Housing Safety Protection Across Syracuse Neighborhoods**

---

## Project Summary

This project evaluates whether housing safety enforcement in Syracuse is aligned with community need. By combining rental inspection records, neighborhood disorder reports, and child poverty indicators, the project will identify areas where vulnerable families may lack adequate housing protection. The final deliverable will be an interactive public map and dashboard that allows residents, policymakers, and community organizations to understand how housing enforcement is distributed across the city. The goal is to transform separate municipal datasets into an accessible civic transparency tool that supports fair and informed decision-making.

---

## Problem Statement

City housing inspection programs exist to protect residents — especially renters and families — from unsafe living conditions. However, residents often question whether enforcement occurs where it is most needed. Some neighborhoods experience more reported disorder, older housing stock, and greater economic vulnerability, which increases the importance of consistent inspections.

This project asks:

> **Is housing safety enforcement reaching Syracuse neighborhoods where vulnerable families live and report the most neighborhood problems?**

Rather than studying crime itself, the project evaluates alignment between community need and city service delivery. If neighborhoods with higher vulnerability and more quality-of-life issues have fewer valid rental inspections, this may indicate service gaps. Conversely, strong alignment would demonstrate effective targeting of enforcement resources.

This information matters to:

* Residents understanding local protections
* City officials prioritizing inspections
* Community organizations planning support programs
* Journalists examining housing equity
* Researchers studying public service delivery

The project focuses on transparency and resource distribution, not labeling neighborhoods as “good” or “bad.”

---

## Data Sources

### 1. Rental Registry – City of Syracuse Code Enforcement

**Role:** Housing protection indicator
**Key Variables:**

* `rr_is_valid`
* `valid_until`
* `NeedsRR`
* Latitude / Longitude

**Strengths:**

* Official enforcement data
* Recently updated

**Limitations:**

* Does not include violation severity details

---

### 2. Part II Crime Data – Syracuse Police Department

**Role:** Neighborhood problem reporting indicator
**Key Variables:**

* Quality-of-life offense categories
* Date
* Latitude / Longitude

**Strengths:**

* Weekly updates
* Represents resident-experienced neighborhood issues

**Limitations:**

* Reported incidents only
* Approximate locations

---

### 3. Kindergarten Readiness & Poverty – Syracuse City School District

**Role:** Community vulnerability indicator
**Key Variables:**

* Poverty percentage
* Readiness rates
* Census tract

**Strengths:**

* Reliable proxy for family vulnerability
* Aggregated and privacy-safe

**Limitations:**

* Indirect socioeconomic measure

---

## Technical Approach

All datasets will be spatially aggregated to the neighborhood level.

### Processing

* Clean geographic coordinates
* Spatial join to neighborhood polygons
* Compute neighborhood metrics:

  * Percentage of valid rental inspections
  * Disorder incident density
  * Child vulnerability score

### Analysis

The project will compare neighborhoods using:

* Ranking comparisons
* Gap detection (high need vs low protection)
* Cluster visualization

### LLM Augmentation

LLMs will be used only for interpretation:

* Generate plain-language neighborhood summaries
* Explain patterns for non-technical audiences
* Perform bias-check prompting on conclusions

Validation will include manual verification of computed metrics and structured reasoning prompts to prevent hallucinated claims.

---

## Deliverable Description

A public-facing interactive dashboard including:

* Syracuse neighborhood map
* Toggleable layers:

  * Housing inspection coverage
  * Reported neighborhood problems
  * Community vulnerability
* Automatically generated plain-English explanations
* Key findings panel summarizing service alignment

The interface will be understandable without technical knowledge and suitable for civic engagement.

---

## Success Criteria

The project succeeds if:

* All datasets integrate correctly at the neighborhood level
* A user can understand their neighborhood in under 30 seconds
* The tool identifies at least one clear service alignment or gap
* LLM explanations accurately reflect data
* Findings are understandable without statistical training
* No misleading conclusions are produced

---

## Timeline

| Week         | Activities / Milestones                                                                                                                                                                                                                                                                                                       |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Week 1**   | **Project Planning & Dataset Review**<br>- Finalize research question and project scope<br>- Identify datasets: Rental Registry, Part II Crime Data, Kindergarten Readiness/Poverty<br>- Document acquisition methods and API endpoints<br>- Store raw datasets and prepare initial data dictionary                           |
| **Week 2**   | **Initial Data Exploration**<br>- Examine dataset quality: missing values, anomalies, coverage<br>- Check geographic completeness and temporal patterns<br>- Start preliminary visualizations to understand distributions (histograms, maps)<br>- Document limitations and biases                                             |
| **Week 3**   | **Data Cleaning & Standardization**<br>- Standardize column names, formats, and data types<br>- Handle missing or inconsistent data<br>- Geocode or validate latitude/longitude where necessary<br>- Start integrating neighborhood boundaries shapefile for spatial joins                                                    |
| **Week 4**   | **Exploratory Spatial Analysis**<br>- Aggregate data to neighborhood level<br>- Compute key metrics:<br>  - % valid rental inspections<br>  - Quality-of-life incident density<br>  - Child vulnerability score<br>- Create initial neighborhood-level maps<br>- Document early patterns and hypotheses                       |
| **Week 5**   | **Advanced Analysis & LLM Integration**<br>- Identify correlations or gaps between enforcement, disorder, and vulnerability<br>- Use LLMs to generate plain-language summaries of patterns<br>- Validate LLM outputs against actual data calculations<br>- Refine analytical methods as needed                                |
| **Week 6**   | **Architecture & Data Pipeline Review**<br>- Document system architecture (data flow, dependencies)<br>- Ensure reproducible pipeline from raw → clean → analyzed<br>- Unit tests for critical calculations<br>- Identify blockers for Week 7+ development                                                                    |
| **Week 7**   | **Visualization Prototyping**<br>- Develop neighborhood map layers:<br>  - Rental inspection coverage<br>  - Neighborhood disorder incidents<br>  - Child poverty indicators<br>- Experiment with interactive elements (hover, toggle layers)<br>- Gather feedback on usability and clarity                                   |
| **Week 8**   | **Working Prototype**<br>- Core functionality operational:<br>  - Neighborhood map interactive<br>  - Dashboard displays key metrics<br>  - LLM-generated summaries integrated<br>- Begin documenting user guide and methodology                                                                                              |
| **Week 9**   | **Gap Analysis & Insight Generation**<br>- Identify neighborhoods with low enforcement relative to need<br>- Highlight interesting patterns or outliers<br>- Generate preliminary conclusions and actionable insights<br>- Validate all visualizations and narratives                                                         |
| **Week 10**  | **Feature Completion & Refinement**<br>- Finalize map interactivity and dashboard layout<br>- Add filters, legends, and explanatory text<br>- Ensure mobile/responsive display<br>- Complete internal QA and edge case handling                                                                                               |
| **Week 11**  | **Documentation & Reporting**<br>- Complete `README.md`, `TECHNICAL.md`, and `METHODOLOGY.md`<br>- Document all assumptions, data limitations, and validation steps<br>- Prepare final exploratory analysis report from Phase 2                                                                                               |
| **Week 12**  | **Final Testing & Polish**<br>- Fix any remaining bugs or inconsistencies<br>- Enhance visual design and user experience<br>- Confirm LLM summaries are accurate and unbiased<br>- Prepare deployment instructions or host dashboard if applicable                                                                            |
| **Week 13+** | **Presentation & Showcase**<br>- Prepare 10-minute presentation:<br>  - Problem and why it matters<br>  - Approach and datasets used<br>  - Key findings (live demo or visualizations)<br>  - Limitations and future work<br>- Optional: share project on Open Data Syracuse page, city communications, or policy discussions |

---

## Risks and Mitigations

**Geographic mismatches** → Aggregate to neighborhood level
**Weak correlations** → Frame as service transparency, not causation
**Proxy limitations** → Clearly document assumptions
**LLM narrative errors** → Human-verified prompt validation
**Missing data areas** → Mark as insufficient data rather than interpret
