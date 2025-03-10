def get_book_text(url):
    with open(url) as f:
       file_contents = f.read()
       return file_contents
    
def count_charactor(text):
    dict1 = {}
    for i in text:
        j = i.lower()
        if j in dict1:
            dict1[j]=dict1[j]+1
        else:
            dict1[j]=1
    return dict1

