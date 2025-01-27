def generate_hashtag(s):
    if not s.strip():
        return False
    hashtag = '#' + ''.join(i.capitalize() for i in s.split())
    if len(hashtag) > 140:
        return False

    return hashtag


print(generate_hashtag('Hello World'))
print(generate_hashtag(''))
print(generate_hashtag('              kek lol arbedol       '))