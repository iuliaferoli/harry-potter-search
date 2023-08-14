# Harry Potter and the Elasticsearch Engine

## Intro to Elasticsearch

## Setup Environment

## Quickstart Tutorial

### Importing Data
* overrwriting the csv details

### Kibana Dashboard

Once our data is imported and we have a view generated, we cn start exploring our data in Discover, or create visualizations in Dashboard - both found under the Analytics tab.

Regardless if you've worked with another BI tool before - Kibana Dashboard is pretty intuitive.

First you want to create a new Dashboard, and start editing it to create visualizations based on your dataset. 
This lets us get a first look at our Harry Potter data. Drag and drop fields to explore different charting options. (see tutorial link for more info)

Here is a quick example of some visuals that might be interesting.

(picture)
In a few minutes, we found out we mostly read about males in Gryffindor, and that most wizards probably cannot produce a patronus. 
However, the most important thing we can learn from the Dashboard is that our data probably needs more cleaning. We can already see duplicates of column values such as "Pure-blood or half-blood", or even columns that are completely missing from our dashboard. 

(picture)

You will notice that not all columns in the dataset show up as fields. We notice the pop-up suggesting full text fields cannot be visualized, which might be the reason why. Therefore, if we want to get more meaningful information, we'll have to start processing our dataset. 

In the next sections we will explore how strings work in Elastic, and how to set up accurate mappings to define our fields and make search easier.

### Discover Queries


Going one step further than the drag and drop tool, we can also get an initial look at our using the KQL language to run some quick searches.

Let's try it out with an easy exampe: 

```
gryffindor
```

This only gives us 5 hits. That doesn't seem consistent with the previous Dashboard view, we know we have a "House" field that's mostly dommuniated by red and gold. 

Take a closer look at those 5 hits. It seems they are all part of text fields rather than the pie-chart values we looked at earlier. This is our first encounter with a very important property: case sensitivity. 

```
Gryffindor
```

Searching for "Gryffindor" instead gives us 38 hits. You can notice in the result we are now getting results both in the "House" column, as well as the text fields from the previous query. Odd, right?

(picture)

The reason for this is that fields such as "Job" and "Skills" have been processed as "text" fields - which are then automatically analyzed by Elastic and lowercased to make searching them easier. While, on the other side, the field "House" has been mapped as a "keyword", which remains case sensitive for more precise queries. 

It's therefore useful to be more prescriptive with what we are searchign for. 
We can specify we want to find the entries with "House: Gryffindor"; or those who have Gryffindor in their skills:

```
Skills: Gryffindor
```
(picture)

In the next sections, we'll finally dive in and look at some core Elasticsearch concepts. Let's clear up "text" from "keyword" and explore our complex fields a little better to run some fun queries.


### Mapping our Index

Finally, let's get to, you know, search. 

### Search Queries


```
GET hp_char/_mapping
```

```json
{
  "hp_char": {
    "mappings": {
      "_meta": {
        "created_by": "file-data-visualizer"
      },
      "properties": {
        "Birth": {
          "type": "text"
        },
        "Blood status": {
          "type": "keyword"
        },
        "Death": {
          "type": "keyword"
        },
        "Eye colour": {
          "type": "keyword"
        },
        "Gender": {
          "type": "keyword"
        },
        "Hair colour": {
          "type": "keyword"
        },
        "House": {
          "type": "keyword"
        },
        "Id": {
          "type": "long"
        },
        "Job": {
          "type": "text"
        },
        "Loyalty": {
          "type": "text"
        },
        "Name": {
          "type": "keyword"
        },
        "Patronus": {
          "type": "keyword"
        },
        "Skills": {
          "type": "text"
        },
        "Species": {
          "type": "keyword"
        },
        "Wand": {
          "type": "text"
        }
      }
    }
  }
}```


