"# searchUsingElasticSearch" 

Internal Search Engine using Elastic Search
====================================

Description
=================================================
This is internal search Engine, which is accomplished using "ElasticSearch" tool for Indexing document. Python Flask as
middle ware interface between UI and ElasticSearch


Prerequisites
================
Python 64bit 2.7
Using Python pip install following packages:
1. pip install flask
2. pip install json
3. pip install elasticsearch

Installation
===========
1. CentOS7
2. Download and untar elasticSearch - https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html
2. Install ElasticSearch - https://dzone.com/articles/elasticsearch-setup-and-configuration
3. Following Getting started with Elastic Search - https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html

Getting Started
=================
1. Using non-root user, start elastic search
2. Start "searchFlaskIndex.py"
3. Open "searchIndex.html"
4. Enter the following:
    - Name of the Document or Link in "Name" field
    - Link of webpage in "Link" field
    - Keywords using we want to search this document in "Keyword" field
    - Incremental value of DocId in "DocId" field
    - Click on "Submit"
5. Will get response from elastic search, where response will be either "created" or "updated"
6. Verify newly indexed document using either, search by "Name" or "Keyword"
7. On response of above, you will get hyperlink of indexed document with description

Created by
===========
- Virendra Ukey
- Email : viruukey@gmail.com 
