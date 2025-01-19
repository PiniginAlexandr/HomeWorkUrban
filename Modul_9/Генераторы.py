def all_variants(text):
    text_len = len(text)
    for length in range(1, text_len + 1):
        for start in range(text_len - length + 1):
            yield text[start:start + length]


a = all_variants('abc')
for i in a:
    print(i)
