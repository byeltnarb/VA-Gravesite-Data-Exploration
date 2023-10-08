
# VA Deceased Gravesite Project

## Introduction

In this project, I worked on analyzing a dataset from the National Cemetery Administration. My main goal was to clean, analyze, and derive insights about gravesites and their associated zip codes for county "Jackson County, Kansas" to present to "American Legion Post 44".

## Dataset Description

The dataset, `National_Cemetery_Administration_Gravesite_Locator_VA_dataset.csv`, contains details about gravesites, including (but not limited to) the associated zip codes. The dataset I ended with was "filter_ja_zip_data.csv", which it a starting point for analyzing the specifc deceased locations within Jackson County, Kansas.

## Tools Used

- Python
- Pandas
- Jupyter Notebooks
- Visual Studio Code

## Challenges

1. **Reading the Large CSV File:** The dataset was extensive, which initially caused issues in loading and analyzing the entire dataset at once. To overcome this, I used pandas functionalities like `nrows` to read a subset of data initially.

2. **Addressing Data Inconsistencies:** Encountered columns with mixed data types, particularly the 'Cemetery ZIP' column. Some zip codes were read as integers, while others, possibly due to leading zeros or non-numeric characters, were read as strings.

3. **Resolving File Path Issues:** Initially faced file path issues when trying to read the CSV file.

## Solutions & Key Takeaways

1. **Data Inspection:** Used methods like `head()`, `tail()`, and `unique()` to inspect data before deep diving into cleaning and analysis.

2. **Data Cleaning:** Converted columns with mixed data types to a consistent type. For instance, the 'Cemetery ZIP' column was converted to a string for uniformity.

3. **Data Analysis:** Derived insights about specific zip codes and their counts.

4. **Path Troubleshooting:** Utilized raw string literals to correctly interpret the file paths in Windows.

5. **Data Saving:** After filtering the required data, saved it in a specific folder for further use.

## Conclusion

Working on this project has strengthened my skills in data engineering, particularly in handling and cleaning large datasets. It's also highlighted the importance of preliminary data inspection before performing any advanced operations.

## Future Work
2023 Sept UPDATE
 - cleaned "src\data_cleaning_ks.ipynb" futher and saved as "src\data_cleaning_ks_cont.ipynb"
 - Introduced insights through HTML visualiztion "dashboardapp\html_dashboard.html"

### On This Dataset
- **Visualization:** Introduce visualization tools to present data in a graphical and more intuitive format.
- **Performance:** Augment code to be more efficient and adept at managing even larger datasets.
- **Advanced Analytics:** Integrate more advanced analytics to derive deeper insights.

### On Data Engineering At Large
- **Data Pipeline Optimization:** Rework the current data processes to embrace real-time data absorption and handling, ensuring smooth integration of any updates to the dataset.
- **Data Validation:** Implement automated systems that will monitor and ensure data accuracy and consistency.
- **Database Collaboration:** Contemplate shifting the refined data to a structured database system, opening doors to enhanced querying capabilities and potential dataset amalgamations.
- **Scalable Systems:** Explore and potentially embrace distributed data frameworks like Apache Spark, guaranteeing scalability for even larger datasets.
- **Versioning the Data:** Strategize and introduce data versioning to ensure traceability, reproducibility, and effortless management of periodic dataset updates.

## Credits/Acknowledgments
Credit goes to the National Cemetery Administration for the dataset and the tools mentioned for facilitating the analysis.

## Preview of Interactive Plots

![summary-statistics](https://github.com/byeltnarb/VA-Gravesite-Data-Exploration/assets/78366874/49f7f613-c1d6-487f-a937-3acf3945dc4a)

![age-at-death](https://github.com/byeltnarb/VA-Gravesite-Data-Exploration/assets/78366874/39e16c3d-254a-41e1-8e13-8ca463413f65)

![age-at-death-line](https://github.com/byeltnarb/VA-Gravesite-Data-Exploration/assets/78366874/da252999-6f4b-42ae-9dc5-32ee3ae83306)

![age-at-death-scatter](https://github.com/byeltnarb/VA-Gravesite-Data-Exploration/assets/78366874/a55ee24c-1bda-4030-acbd-9c06ce19b99d)

