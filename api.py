#!restMicroservice/bin/python
from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta


app = Flask(__name__)

def get_trending_repo():
    '''
        function to fetch trending repos from github api without authentication
    '''
    headers = { 
    'Content-type' :'application/json',
    'Accept' : 'application/vnd.github.v3+json'
    }
    timer = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    req = requests.get("https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc?page=1&per_page=100".format(timer), headers=headers)
    if req.status_code == 200:
        return req.json()['items']
    return 1


repos = get_trending_repo()



@app.route("/trend/languages", methods=['GET'])
def get_languages():
    '''
        list all (main) languages used in trending repos
    '''
    # repos = get_trending_repo()
    if repos != 1:
        languages_list = [repo['language'] for repo in repos if repo['language'] != None]
        dico_langues = {lang : languages_list.count(lang) for lang in languages_list}
        d_sorted = sorted(dico_langues.items(), reverse=True, key=lambda x: x[1])
        languages_occurence = {i[0]: i[1] for i in d_sorted}
        if languages_occurence != {}:
            return jsonify(languages_occurence)
        return jsonify({'message': 'No language were found !'})
    return jsonify({'message': 'Something went wrong !'})

@app.route("/trend/languages/<language_name>", methods=['GET'])
def get_languages_repos(language_name):
    '''
        list all repos(among the trending) which use the given language
    '''
    if repos != []:
        given_language_repos = {language_name: [r['html_url'] for r in repos if r['language'] != None and r['language'].lower() == language_name.lower()]}
        return jsonify(given_language_repos)
    pass



if __name__ == '__main__':
    app.run(debug=True)
