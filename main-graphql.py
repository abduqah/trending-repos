import requests
import json
from sys import exit
from datetime import date, timedelta
from decouple import config
from string import Template

def main():
  check_token_exists()

  date_30days_ago = date.today() - timedelta(30)

  response = call_github_api(date_30days_ago)
  return get_statistics(response)

def call_github_api(date):
  print('Real process started', sep='\n')

  query = Template("""{
    search(type: REPOSITORY, query: "created:>$date sort:stars-desc", first: $numOfResults) {
      nodes {
        ... on Repository {
          name
          url
          languages(first: 100) {
            nodes {
              name
            }
          }
        }
      }
    }
  }""")

  r = requests.post("https://api.github.com/graphql", json={'query': query.substitute(date=date, numOfResults=100)},headers={'Authorization': 'token %s' % config('TOKEN')})
  json_data = json.loads(r.text)

  return json_data['data']['search']['nodes']


def get_statistics(data):
  languages = {}

  for repo in data:
    for lang in repo['languages']['nodes']:
      try:
        language_obj = languages[lang['name']]
        language_obj['count'] += 1
        language_obj['repos_list'].append(repo['url'])
      except:
        languages[lang['name']] = {'count': 1, 'repos_list': [repo['url']]}
        print('New language added: %s' % lang['name'], sep='\n')
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
  


with open('GraphQL-statistics.json', 'w') as file:
  json.dump(main(), file)

