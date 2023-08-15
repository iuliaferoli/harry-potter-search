![](img/LOGO.png)
# Harry Potter and the Elasticsearch Engine

This project covers serch use cases on Harry Potter text databases, with a focus on python integrations.

The goal on phase one is to create a index where each document is a Harry Potter character with their attributes. This index can them be used to create customized search queries to identify subsets of characters with particular properties.

This example project covers the basic introductory concepts of elasticsearch and kibana. 

#### Implemented features and planned additions
- [X] HP characters index & search
- [ ] HP characters index - python client interface for search
- [ ] HP book corpus word2vec embeddings and similairy mapping
- [ ] HP and the Generative AI


## Setup Environment

Requirements
Installation of Elasticsearch (either local or on cloud) [see docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

For python environment, recommend to set up a virtual environment [see docs](https://docs.python.org/3/library/venv.html). 
Requirements: pandas. 

## Harry Potter Characters Index | Intro to Elasticsearch

### [0 Cleaning Data.ipynb](/0.%20Cleaning%20Data.ipynb)
Python notebook for some essential data cleaning with pandas dataframes.

### [0.5 Importing Data](/0.5.%20%20Importing%20Data.md)
Instructinos for adding data to the elastic cluster.

### [1 Kibana Dashboard](/1.%20Kibana%20Dashboard.md)
Short intro to Dashboards and visualizations in Kibana.

### [2 Discover Queries](/2.%20Discover%20Queries.md)
Short intro to Discover and KQL.

### [3 Index Mapping](/3.%20Index%20Mapping)
Working with Console / dev tools, intro to data types in elastic.

### [4 Search Magic](/4.%20Search%20Magic.md)
Building requests and intro to queries.
