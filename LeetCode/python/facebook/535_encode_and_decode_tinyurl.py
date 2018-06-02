# coding=utf-8

# 2018-06-02 00:44
# 2018-06-02 00:58

class Codec:

    def __init__(self):
        self.count = 0
        self.long_to_short = dict()
        self.short_to_long = dict()
        self.root = "http://tinyurl.com/"
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        if longUrl in self.long_to_short:
            return self.root + self.long_to_short[longUrl]
        else:
            tiny = str(self.count)
            self.long_to_short[longUrl] = tiny
            self.short_to_long[tiny] = longUrl
            tiny = self.root + str(self.count)
            self.count += 1
            return tiny
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        pos = shortUrl.rfind("/")
        if shortUrl[0: pos + 1] == self.root:
            long = self.short_to_long.get(shortUrl[pos + 1:], "")
            return long 
        return ""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == "__main__":
    s = Codec()
    tiny = s.encode("www.google.com")
    long = s.decode(tiny)
    print tiny
    print long
    
    tiny = s.encode("www.google.com")
    long = s.decode(tiny)
    print tiny
    print long
    
    tiny = s.encode("www.facebook.com")
    long = s.decode(tiny)
    print tiny
    print long
    
    long = s.decode("www.abc.com")
    print long
    
    long = s.decode("www.abc.com/123")
    print long
    
    long = s.decode("http://tinyurl.com/")
    print long
    
    long = s.decode("http://tinyurl.com/1")
    print long
    
    long = s.decode("http://tinyurl.com/10")
    print long