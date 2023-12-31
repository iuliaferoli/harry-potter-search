![](img/LOGO.png)
# Harry Potter and the Elasticsearch Engine

This project covers serch use cases on Harry Potter text databases, with a focus on python integrations.

### Part 1: Intro to Elasticsearch [0](/0.%20Cleaning%20Data.ipynb) --> [4](/4.%20Search%20Magic.md)
Create a index where each document is a Harry Potter character with their attributes. This index can them be used to create customized search queries to identify subsets of characters with particular properties.

This example project covers the basic introductory concepts of elasticsearch and kibana. 

### In Part 2: Python Clients [5](/5.%20Python%20Wrapper.ipynb) --> [9](/9.%20ELSER%20Semantic%20Search.ipynb)
Introduce the python client to communicate with the Elasticsearch engine via code. Create an index from the first Harry Potter movie script to use for more complex, natural language queries.
Import models with the Eland python client allowing us to do sentiment analysis and embeddings.
Use ELSER for semantic search
Combine the different search techniques together


### Implemented features and planned additions
- [X] HP characters index & search
- [X] HP characters index - python client interface for search
- [X] HP sentiment analysis on movie subtitles
- [X] Embeddings and semantic search with ELSER
- [ ] Python-DSL client
- [ ] Observability & Monitoring


[![Watch the video](img/yb.png)](https://www.youtube.com/watch?v=avxqGSPyKOA)



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

## Harry Potter Movie Dialogue Index | Intro to Elastic Python Client

### [5 Python Wrapper](/5.%20Python%20Wrapper.ipynb)
Working with the python client to build an index and mapping, bulk ingest documents, and run queries.

### [7 Eland and NLP - Sentiment analysis](/7.%20Eland%20Client%20&%20%20NLP.ipynb)
Importing models from huggingface using the ELand client. Running sentiment analysis on our index.

### [8 Embeddings and Vector search](/8.%20Vector%20Search.ipynb)
Importing an embedding model and using the vector space to run semantic search.

### [9 ELSER Semantic Search](/9.%20ELSER%20Semantic%20Search.ipynb)
Upgrading semantic search experience with ELSER and combining "classic" elastic searches with sentiment and embeddings for extra dimensions.
