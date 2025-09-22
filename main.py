from src.api.news_api import NewsAPIClient
from src.helpers.news_helpers import (
    display_articles,
    save_results_to_csv
)


def main():
    """Main function to demonstrate News API"""

    keywords = ["trump", "biden", "python", "ai", "climate change"]

    try:
        client = NewsAPIClient()

        for keyword in keywords:
            print(f"===== Searching for every news article with Keyword: '{keyword}' =====")

            news_data = client.search_everything(keyword, page_size=5)

            if news_data:
                display_articles(news_data)
                save_results_to_csv(news_data, keyword)
            else:
                print(f"No data found for keyword: {keyword}")

            print("\n" + "=" * 80 + "\n")

    except ValueError as e:
        print(f"Configuration error: {e}")
        print("API_KEY is not correctly set")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
