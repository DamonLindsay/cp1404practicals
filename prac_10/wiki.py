import wikipedia


def main():
    """This program will continuously prompt the user for a Wikipedia page title and print its summary."""
    user_input = input("Enter a page title (blank to exit): ")
    while user_input != "":
        get_wikipedia_summary(user_input)
        user_input = input("Enter a page title (blank to exit): ")


def get_wikipedia_summary(page_title):
    """Get the summary of a Wikipedia page and print the title, summary, and URL."""
    try:
        page = wikipedia.page(page_title)

        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error: {e.options}")
    except wikipedia.exceptions.HTTPTimeoutError as e:
        print(f"HTTP Timeout Error: {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"Page Error: {e}")


if __name__ == '__main__':
    main()
