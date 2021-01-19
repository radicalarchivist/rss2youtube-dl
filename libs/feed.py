import feedparser

class Feed:
    def __init__(self,feed):
        try:
            self.feed = feedparser.parse(feed).entries
        except:
            self.feed = False

    def download(self):
        if self.feed:
            return [{'title':post.title,'href':post.links[0]['href']} for post in self.feed]
        else:
            return False

    def test(self):
        if self.feed:
            for post in self.feed:
                print(post.title,end="\n\n\n")
        else:
            print('something went wrong')

if __name__ == "__main__":
    feed = Feed('https://rss.outsider.press/public.php?op=rss&id=-1460&key=xexmt25ec46090f2c8c')
    for item in feed.download():
        print('Title:',item['title'])
        print('Path:',item['href'])
