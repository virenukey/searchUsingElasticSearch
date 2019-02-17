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
4. Download and install Postman - https://www.getpostman.com/
5. Using postman, index document. Follow following example:
URL - http://192.168.234.129:9200/qa_kb/link/1?pretty [http://<elasticEndpoint:port>/index/type/docId]


Getting Started
=================
1. Using non-root user, start elastic search
2. Index few documents .e.g
Url - http://192.168.234.129:9200/qa_kb/link/1?pretty 
Header - ContentType: application/json
Body:
{
  "name": "python memory management",
  "link": "https://realpython.com/python-memory-management/",
  "keyword": "memory management"
}
3. Start "searchFlask.py"
4. Open "search.html"
5. Enter text "memory management" in text box
6. Will get indexed document in response

Note
========
Enhance this tool, for indexing PDF, word document. Index new doc type. For this poc I have used "link" as doc type,
because I am indexing hyperlinks

Created by
===========
- Virendra Ukey
- Email : viruukey@gmail.com