# today's solution
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    paragraph = ''.join([c if c.isalpha() else " " for c in paragraph.lower()]).split()
    paragraph = [word for word in paragraph if word not in banned]
    
    cnt = { word: 0 for word in paragraph }
    for word in paragraph:
        cnt[word] += 1
    # print(cnt)
    return max(cnt, key=lambda x: cnt[x])
        
# past: 2021-11-07
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    paragraph = re.sub(r"[!?',;.]", ' ', paragraph).lower()
    paragraph = [word for word in paragraph.split() if word not in banned]

    occurence = {}
    for word in paragraph:
        if word in occurence: occurence[word] += 1
        else: occurence[word] = 1

    return max(occurence, key = lambda word: occurence[word])

# most voted:
def mostCommonWord(self, p, banned):
    ban = set(banned)
    words = re.findall(r'\w+', p.lower())
    return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

# another discovery: fastest
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    para = re.sub('[^A-Za-z0-9]+', ' ', paragraph)
    para = para.split(' ')
    para = [i.lower() for i in para if i.lower() not in banned if i != '']
    return max(para, key = para.count)