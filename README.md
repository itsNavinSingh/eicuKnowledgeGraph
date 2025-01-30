# eICU Knowledge Graph

This repository contains the code and resources for building a Knowledge Graph from the eICU Collaborative Research Database. The project aims to extract meaningful relationships and insights from electronic health records (EHR) and represent them in a structured graph format for advanced analysis and querying.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Pipeline](#data-pipeline)

---

## Introduction

The **eICU Knowledge Graph** project transforms raw eICU data into a structured knowledge graph, enabling advanced querying, analysis, and visualization of patient health records. The knowledge graph captures relationships between patients, diagnoses, treatments, medications, and other medical entities, making it a powerful tool for healthcare analytics and research.

---

## Features

- **Data Extraction**: Extract and preprocess data from the eICU database.
- **Entity Recognition**: Identify key medical entities (e.g., patients, diagnoses, medications).
- **Relationship Extraction**: Define and extract relationships between entities.
- **Graph Construction**: Build a knowledge graph using a graph database (e.g., Neo4j).
- **Query Interface**: Query the knowledge graph for insights and patterns.
- **Visualization**: Visualize the graph structure and relationships.

---

## Installation

### Prerequisites
- Python 3.8+
- pip installed
- eICU Collaborative Research Database access

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/itsNavinSingh/eicuKnowledgeGraph.git
   cd eicuKnowledgeGraph
   ```
2. Move dataset directory to `eicuKnowledgeGraph` directory
#### For windows
3. Run the `execute_windows.bat` file
    ```bash
    execute_windows.bat
    ```
#### for Linux/macOS
3. Make the `execute_linux_mac.sh` File Executable and Run the Script
    ```bash
    chmod +x execute_linux_mac.sh
    ./execute_linux_mac.sh
    ```
#### Common command
4. It will ask to `Enter the input directory path`
5. Enter the Relative path of dataset directory.
6. It will generate all the `.ttl` file in `result` directory.


---


## Usage
1. The script will generate .ttl (Turtle) files in the result directory. These files represent the knowledge graph and can be imported into a graph database like Neo4j for further querying and analysis.

2. Once the .ttl files are generated, you can load them into a graph database such as Neo4j. Use Cypher queries to explore relationships between medical entities (e.g., patients, diagnoses, medications). This enables advanced analytics and can help uncover patterns in healthcare data.


---


## Data Pipeline
The `eicu Knowledge Graph` uses a data pipline to extract, preprocess, and transform raw eICU data into a structured knowledge graph. This section outlines the steps and components involved in the data pipeline.
### `Data Ingestion`
The first step in the pipeline is the ingestion of raw data from the `eICU Collaborative Research Database`. The data consists of various tables containing information on patient demographics, diagnoses, treatments, medications, vital signs, and more. This raw data is in CSV format.
* `Source Data` :
        The eICU dataset includes multiple files that contain structured data across several tables.
* `Data Access` :
        To access the eICU data, users need to register with the [eICU Research Institute](https://eicu-crd.mit.edu) and obtain the dataset.
### `Data Preprocessing`
Once the raw data is ingested, it needs to be cleaned and preprocessed. This step involves the following tasks:
* `Data Cleaning` :
    Handling missing values, removing duplicate records, and converting data types to ensure consistency.
* `Data Transformation` :
    Converting the raw data into a structured format suitable for graph construction. This includes normalizing and categorizing various medical entities.
The preprocessing is done using the provided scripts. It process the data and prepare it for next step.
