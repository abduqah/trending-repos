import requests
import json
from sys import exit
from datetime import date, timedelta
from decouple import config

def main():
  check_token_exists()

  date_30days_ago = date.today() - timedelta(30)

  response = call_github_api(date_30days_ago)
  return get_statistics(response)

def call_github_api(date):
  print('Real process started', sep='\n')
  r = requests.get("https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc&per_page=100".format(date))
  json_data = json.loads(r.text)

  return json_data['items']


def get_statistics(data):
  languages = {}

  for repo in data:
    r = requests.get(repo['languages_url'], headers={'Authorization': 'token %s' % config('TOKEN')})
    json_data = json.loads(r.text)

    for lang, uuid in json_data.items():
      try:
        language_obj = languages[lang]
        language_obj['count'] += 1
        language_obj['repos_list'].append(repo['url'])
      except:
        languages[lang] = {'count': 1, 'repos_list': [repo['url']]}
        print('New language added: %s' % lang, sep='\n')
        pass

  return languages

def check_token_exists():
  try:
    if len(config('TOKEN')) == 0:
      print('Please add valid token')
      exit(1)
  except:
    print('Please add .env file with token provided inside. check .env.example')
    exit(1)
    pass
  


with open('statistics.json', 'w') as file:
  json.dump(main(), file)