class BaseConfig:

    """This class contatins the base cofiguration (ex.api_token,base_url).
    You have to provide github api token and api base url(https://api.github.com) for complete the
    configuration properly."""

    def __init__(self,api_token="",base_url="",user_name=""):
        self.api_token = api_token
        self.base_url = base_url
        self.user_name = user_name
    
    # Method for conplete the configuration
    def config_github(self,api_token,base_url,user_name):
        api_token = self.api_token
        base_url = self.base_url
        user_name = self.user_name
        
    

