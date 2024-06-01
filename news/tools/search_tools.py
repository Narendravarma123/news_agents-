# # import json
# # import os

# # import requests
# from langchain.tools import tool


# import json

# import os

# import requests
# # from langchain.tools import tool
# #serpapi

# class SearchTools():
#     @tool("Search the internet")
#     def search_internet(query):

#         """Useful to search the internet
#         about a a given topic and return relevant results"""
#         print("Searching the internet...")
#         top_result_to_return = 5
#         url = "https://serpapi.com/search.json"
#         params = {
#             "engine": "google_news",
#             "q":query,
#             "gl": "us",
#             "api_key": "a978655295f1ff941dbcf953765d394414def1aa2507b8406ffa7a01c86eb453"
#         }
#         response = requests.get(url, params=params)
#         # print(response.json())
        

#         if 'news_results' in response.json():
#             results = response.json()['news_results']
#             string = []
#             # print("Results:", results[:top_result_to_return])
#             for result in results[:top_result_to_return]:
#                 try:
#                     # Attempt to extract the date
#                     date = result.get('date', 'Date not available')
#                     string.append('\n'.join([
#                         f"Title: {result['title']}",
#                         f"Link: {result['link']}",
#                         f"Date: {date}",  # Include the date in the output
#                         f"Snippet: {result['thumbnail']}",
#                         "\n-----------------"
#                     ]))
#                     # print(string)
#                 except KeyError:
#                     next

#             return '\n'.join(string)
#         else:
#             return "No tools found in the response."




import json
import os

import requests
from langchain.tools import tool


class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        print("Searching the internet...")
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps(
            {"q": query, "num": top_result_to_return, "tbm": "nws"})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        else:
            results = response.json()['organic']
            string = []
            print("Results:", results[:top_result_to_return])
            for result in results[:top_result_to_return]:
                try:
                    # Attempt to extract the date
                    date = result.get('date', 'Date not available')
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Date: {date}",  # Include the date in the output
                        f"Snippet: {result['snippet']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)