import pyshorteners


def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url


def main():
    original_url = input("Enter the URL to shorten: ")

    try:
        shortened_url = shorten_url(original_url)
        print("\nOriginal URL:", original_url)
        print("Shortened URL:", shortened_url)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
