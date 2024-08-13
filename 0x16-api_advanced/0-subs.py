import requests

def number_of_subscribers(subreddit):
    # Define the URL with the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid request blocking by Reddit
    headers = {'User-Agent': 'my-reddit-subscriber-script/0.1'}

    try:
        # Make the GET request to Reddit API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If subreddit is invalid or doesn't exist, return 0
            return 0
    except requests.RequestException:
        # Handle any requests-related errors (like network issues)
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    subscribers = number_of_subscribers(subreddit)
    print(f"The subreddit r/{subreddit} has {subscribers} subscribers.")
