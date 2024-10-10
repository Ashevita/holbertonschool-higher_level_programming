#!/usr/bin/env python3
import requests
import csv

# Function to fetch and display 


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    # If the request was successful
    if response.status_code == 200:
        # Convert the data to JSON format
        posts = response.json()

        # Iterate through the posts and print their titles
        for post in posts:
            print(f"{post['title']}")

# Function to fetch and save posts into a CSV file


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them into a CSV file.
    Each post is saved with its ID, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # If the request was successful
    if response.status_code == 200:
        # Convert the data to JSON format
        posts = response.json()

    # Structure the data as a list of dictionaries
    data = [{'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts]

    # Write the data into a CSV file
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(data)

    print("Posts have been saved to 'posts.csv'.")
