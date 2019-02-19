from __future__ import print_function
from flask import Flask, render_template, request,jsonify, Response, json
from elasticsearch import Elasticsearch
from ordered_set import OrderedSet
#import json

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('search.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/index', methods=['POST'])
def index():
    docId = request.form['docId']
    name = request.form['name']
    link = request.form['link']
    link = "<a href=\"" + link + "\"" + ">" + link + "</a>"
    keyword = request.form['keyword']
    es = Elasticsearch([{'host':'192.168.234.129','port':9200}])
    res = es.index(index="qa_kb", doc_type="link", id = docId, body={"name":name, "link":link, "keyword":keyword})
    return res['result']

@app.route('/search', methods=['POST'])
def search():
    searchTearm = request.form['searchbox']
    es = Elasticsearch([{'host':'192.168.234.129','port':9200}])
    res = es.search(index="qa_kb", doc_type="link", body={"query": {"match": {"keyword": searchTearm}}})
    if res["hits"]["hits"]:
        a = []
        for i in res["hits"]["hits"]:
            a.append(i['_source']['link'])
        list_set = OrderedSet(a)
        str1 = '<br/>'.join(map(str, list_set))
        return  str1
    else:
        return "No search found"

@app.route('/name', methods=['POST'])
def name():
    searchTearm = request.form['namesearchbox']
    es = Elasticsearch([{'host':'192.168.234.129','port':9200}])
    res = es.search(index="qa_kb", doc_type="link", body={"query": {"match": {"name": searchTearm}}})
    if res["hits"]["hits"]:
        a = []
        for i in res["hits"]["hits"]:
            a.append(i['_source']['link'])
        list_set = OrderedSet(a)
        str1 = '<br/>'.join(map(str, list_set))
        return  str1
    else:
        return "No search found"

if __name__ == '__main__':
   app.run(debug = True)

