# Personalized Life Consultant

This project leverages advanced natural language processing and machine learning techniques to generate personalized reports that offer insights and suggestions on how to potentially increase one's life expectancy based on individual lifestyle and preferences. The project stands out with its integration of the txtai library for semantic search and OpenAI's GPT-4 engine for dynamic suggestion generation.

## Project Overview

This Python application is crafted to exhibit proficiency in several technical areas, including:

- **Python Programming:** The backbone of this application, demonstrating adeptness in Python.
- **Natural Language Processing (NLP):** Leveraging NLP techniques for semantic analysis using txtai.
- **Machine Learning:** Utilizing machine learning for semantic search to find the most relevant factors from a dataset.
- **OpenAI API Integration:** Integrating with OpenAI's GPT-4 for dynamic and AI-driven suggestion generation.
- **PDF Reporting:** Implementing report generation in PDF format, showcasing the ability to work with libraries to create visual outputs from a script.

## Features

- **Semantic Search with txtai:** Extracts the most relevant factors affecting life expectancy based on user input using txtai's semantic search capabilities.
- **GPT-3/4 Integration:** Uses the GPT-3/4 engine to dynamically create personalized suggestions based on the factors identified through semantic search.
- **Professional PDF Reports:** Generates a professional-looking PDF report encapsulating all the personalized suggestions.

## Exploratory Data Analysis (EDA)

Before diving into the development of the main functionalities of this application, a thorough exploratory data analysis was conducted to understand the dataset and derive meaningful insights from it. This section outlines the key steps and findings from the EDA process.

### Dataset Overview

The dataset used in this project contains a range of factors that are believed to influence life expectancy. Each record in the dataset contains a description of a factor along with a value indicating the potential years gained or lost in life expectancy associated with that factor.

### Data Cleaning

Initial steps included cleaning the dataset to remove any inconsistencies and prepare it for analysis. This involved:
- Handling missing values
- Removing duplicates
- Normalizing text data 

### Data Visualization

To gain a deeper understanding of the data, various visualizations were created to:
- Identify the distribution of factors affecting life expectancy
- Visualize the potential years gained or lost associated with different factors

[EDA_Semantic_Therapist.png]

### Feature Engineering

Feature engineering was carried out to create meaningful features from the existing data, which were later used in the semantic analysis process. This involved:
- Tokenizing text data
- Extracting key phrases and terms

### Insights Derived

Some of the critical insights derived from the EDA include:
- Identification of key factors that have a significant impact on life expectancy
- Understanding the correlation between different factors

### Tools and Libraries Used

The following tools and libraries were utilized in the EDA process:
- **Pandas:** For data manipulation and analysis.
- **Matplotlib/Seaborn:** For creating visualizations to understand the data better.

### Notebooks and Scripts

All the notebooks and scripts used during the EDA process are available in the `eda` folder in this repository. Feel free to explore them to understand the dataset deeply and to see the visualizations created during the analysis.

### Conclusion

The EDA process was pivotal in shaping the development of the application by providing a clear understanding of the dataset's structure and the relationships between different factors. It served as the foundation upon which the semantic analysis and report generation functionalities were built.

We encourage contributors and users to delve into the EDA process to garner a deeper understanding of the data and the initial analysis carried out in this project.


## Installation

Before you run the script, install the necessary Python packages using the following command:

```sh
pip install pandas, txtai, openai, seaborn, matplotlib
