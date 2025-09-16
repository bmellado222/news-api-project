import os
import requests
from dotenv import load_dotenv


class NewsAPIClient:
    """Client for NewsAPI.org"""

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        self.base_url = "https://newsapi.org/v2"

        if not self.api_key:
            raise ValueError("API_KEY not found")

    def search_everything(self, keyword, **kwargs):
        """
        :param self: url & api key
        :param keyword: The searched term
        :param kwargs: Additional parameters from API like page_size and language
        :return: JSON response from News API
        """

        print(self.base_url)

        url = f"{self.base_url}/everything"

        params = {
            'q': keyword,
            'apiKey': self.api_key,
            'pageSize': kwargs.get('page_size', 100),
            'language': kwargs.get('language', 'en'),
            'sortBy': kwargs.get('sort_by', 'publishedAt')
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error from API request: {e}")
            return None
        except ValueError as e:
            print(f"Error from JSON response: {e}")
            return None
