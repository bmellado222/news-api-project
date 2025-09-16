# import json
# import csv
# from datetime import datetime
# import os
# ^ ALL For later ^

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

# def save_results_to_csv:
