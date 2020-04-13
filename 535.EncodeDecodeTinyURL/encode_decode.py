class Codec:
    def __init__(self):
        self.alphabets = string.ascii_letters + string.digits
        self.url_to_code = {}
        self.code_to_url = {}
        
        
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        while(longUrl not in self.url_to_code):
            code = "".join(random.choice(self.alphabets) for _ in range(3))
            tiny_url = "http://tinyurl.com/" + code
            if code not in self.code_to_url:
                self.url_to_code[longUrl] = code
                self.code_to_url[code] = longUrl
            
        return tiny_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        x = shortUrl.split("/")
        return self.code_to_url[x[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))