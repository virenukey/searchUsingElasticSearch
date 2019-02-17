from __future__ import print_function
from flask import Flask, render_template, request,jsonify, Response, json
from elasticsearch import Elasticsearch
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

@app.route('/search', methods=['POST'])
def search():
    searchTearm = request.form['searchbox']
    es = Elasticsearch([{'host':'192.168.234.129','port':9200}])
    res = es.search(index="qa_kb", doc_type="link", body={"query": {"match": {"keyword": searchTearm}}})
    if res["hits"]["hits"]:
        a = []
        for i in res["hits"]["hits"]:
            a.append(i['_source']['link'])
        str1 = "\n,\r\n".join(a)
        return  str1
    else:
        return "No search found"

if __name__ == '__main__':
   app.run(debug = True)