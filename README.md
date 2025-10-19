# 📰News Trends Project📰

This script was created with the intention of gathering data over a period of seven days from [NewsAPI.org](https://newsapi.org/) and determining the rise and fall of five news topics, which is then visualized in Power BI. The gathering of data is automated through the use of Windows Task Scheduler.
## Acknowledgements

>**/data**

Contains the script's collected data, the collected data is stored as a .csv file.

There are three main attributes to data collected: the keyword used to search the News API, the total results from that keyword API call, and the date for when the keyword was searched.
>**/src/api**

Houses the API client for NewsAPI.org, requires an API Key & API URL, filtered for news outlets that are English based. Data recieved is stored as a .json file.

>**/src/helpers**

Contains the functions for properly formatting & displaying the data retrieved from calling the News API, as well as the function for storing the retrieved data and converting it into a .csv file.

>**/src/visualization**

Contains graphs created from the search results collected over a period of 7 days. These images were created with the assistance of Power BI.

>**main.py**

Houses the actual keywords that are used during API calls, fires up every other function in the script.

keywords = ["stock market", "israel", "climate change", "uk", "china"]