import feedparser

RedditData = feedparser.parse('https://old.reddit.com/r/sports/.rss?limit=100&t=month')
values = []
try:
    for i, submission in enumerate(RedditData.entries):
        print(submission.title)
        resp = ""
        while resp not in ['y', 'n', 'p']:
            resp = input('{}/{}\tvalid (y), invalid (n), or pass(p)? '.format(i + 1, len(RedditData.entries))).strip().lower()
        if resp == 'p': 
            continue
        values.append("{}: {}".format(resp, submission.title))
except KeyboardInterrupt:
    with open('output.txt', 'w') as ot:
        ot.writelines('\n'.join(values))
    print('Output {} entries'.format(len(values)))

