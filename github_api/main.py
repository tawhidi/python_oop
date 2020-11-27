import requests
import pprint
from config import BaseConfig

api_token = "fc304d47a1272aab2df33d0dab5660dd9902524e"
base_url = "https://api.github.com"
user_name = "tawhidi"
config = BaseConfig(api_token,base_url,user_name)

class GithubMain:
    """Here is some api implementations of Github API"""

    # Method for get all issues
    def show_all_issues(self,repo_name):
        headers = {
            'Authorization': 'tokens ' + config.api_token,
            'Accept': 'application/vnd.github.v3+json'
        }
        api_url = f"{config.base_url}/repos/{config.user_name}/{repo_name}/issues"
        data = requests.get(api_url,headers=headers).json()
        return pprint.pprint(data)

    # Method for get git hub feeds
    def get_feeds(self):
        headers = {
            'Authorization': 'tokens ' + config.api_token,
            'Accept': 'application/vnd.github.v3+json'
        }
        api_url = f"{config.base_url}/events"
        data = requests.get(api_url,headers=headers).json()
        return pprint.pprint(data)

    # Method for show pull request list of specific repository
    def show_all_pull_request(self,repo_name):
        headers = {
            'Authorization':'tokens ' + config.api_token,
            'Accept': 'application/vnd.github.v3+json'
        }
        api_url = f"{config.base_url}/repos/{config.user_name}/{repo_name}/pulls"
        data = requests.get(api_url,headers=headers).json()
        return pprint.pprint(data)

    # Method for specific user Github repository
    def get_user_repository(github_user):
        headers = {
            'Authorization':'tokens ' + config.api_token,
            'Accept': 'application/vnd.github.v3+json'
        }
        api_url = f"{config.base_url}/users/{github_user}/repos"
        data = requests.get(api_url,headers=headers).json()
        return pprint.pprint(data)




main = GithubMain
test = main.create_repository('tawhidi','api-test-repos')
pring(test)

# main = GithubMain()
# # print(main.show_all_issues('Online-Lab'))
# # print(main.get_feeds())
# print(main.show_all_pull_request('Online-Lab'))
