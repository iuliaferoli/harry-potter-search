from helper_functions import connect_client, semantic_search
from flask import Flask, render_template, request
from datetime import datetime

index = "hp_scripts_final"
model_id = "sentence-transformers__msmarco-minilm-l-12-v3"

client = connect_client()

app = Flask(__name__)

@app.route('/')
def search():
   return render_template('search.html')

@app.route('/search' ,methods = ['POST', 'GET'])
def show_search_term():
    if request.method == 'POST':
        # getting the query from the user
        question = request.form["question"]
        # running the semantic search model and getting the results from Elasticsearch
        answer = semantic_search(question, client=client,  model_id=model_id, index=index)
       
        # Logging the search & response in a separate index
        document = {"Query" : question, "Response" : answer, "date" : datetime.now()}
        response = client.index(index = "historical_searches", document = document)
        #print(response)

        # Returning the template for the user to view their results
        return render_template('search_result.html', answer=answer, question =question)

@app.route('/history')
def show_history():
   response = client.search(index = "historical_searches", sort=[{"date" : {"order": "desc"}}])
   return render_template('history.html', response = response["hits"]["hits"])