from src.api.news_api import NewsAPIClient
from src.helpers.news_helpers import (
    display_articles
    # save_results_to_csv
)


def main():
    """Main function to demonstrate News API"""

    try:
        client = NewsAPIClient()

        print("===== Searching for every news article with Keyword: 'python' =====")
        news_data = client.search_everything("trump", page_size=5)

        if news_data:
            display_articles(news_data)

        print("\n" + "=" * 80 + "\n")

        print("===== Searching for every news article with Keyword: 'ai' =====")
        ai_news = client.search_everything(
            "ai",
            page_size=3,
            language="en",
            sort_by="popularity",
        )

        if ai_news:
            display_articles(ai_news)

        print("\n" + "=" * 80 + "\n")

    except ValueError as e:
        print(f"Configuration error: {e}")
        print("API_KEY is not correctly set")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
