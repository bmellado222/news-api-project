import os
import csv
from datetime import datetime


def display_articles (news_data, max_description_length=200):
    """
    Display news articles in a readable format for testing purposes, mostly

    :param news_data: JSON response from News API
    :param max_description_length: Max Length of displayed article description
    :return:
    """

    if not news_data or news_data.get('status') != 'ok':
        print("No news data found")
        return

    articles = news_data.get('articles', [])
    total_results = news_data.get('totalResults', 0)

    print(f"\nFound {total_results} articles")
    print("-" * 80)

    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article.get('title', 'No title')}")
        print(f"   Source: {article.get('source', {}).get('name', 'Unknown')}")
        print(f"   Published: {article.get('publishedAt', 'Unknown')}")

        description = article.get('description', 'No description')
        if len(description) > max_description_length:
            description = description[:max_description_length] + "..."
        print(f"   Description: {description}")
        print(f"   URL: {article.get('url', 'No URL')}")


def save_results_to_csv(news_data, keyword, filename="search_results.csv"):
    """
    Saves article results to CSV file.

    :param news_data: JSON response from the News API.
    :param keyword: The keyword used for the search.
    :param filename: The file the data is stored. defaults 'search_results.csv'.
    :return: str: Path to saved file.
    """
    if not news_data or news_data.get('status') != 'ok':
        print("No valid news data to save")
        return None

    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_dir = os.path.join(project_root, 'data')

    os.makedirs(data_dir, exist_ok=True)

    filepath = os.path.join(data_dir, filename)

    current_date = datetime.now().strftime("%Y-%m-%d")

    total_results = news_data.get('totalResults', 0)

    try:
        file_exists = os.path.exists(filepath)

        with open(filepath, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'keyword', 'total_results', 'date'
            ])

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'keyword': keyword,
                'total_results': total_results,
                'date': current_date
            })

        print(f"Search results saved to: {filepath}")
        return filepath

    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return None
