#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# There are infinitely many solutions to this systems design problem
# My approach was to store them with the key being a unique primary key that
# maps to both the short and long url. This way there cannot be any collisions.
# I just use the pk and convert it by using the 62 alphanumeric characters.
# Likewise to decode, I do the process in reverse!
#-------------------------------------------------------------------------------

class Codec:
    pk = 0
    dictionary = "abcdefghijklmnopqrstuvwxyzAB" + \
        "CDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    mappings = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        # Generate a new suffix using the unique primary key
        pk = self.pk+1
        suffix = ""
        
        while pk:
            suffix = self.dictionary[(pk%62)-1] + suffix
            pk //= 62
        
        # Store new encoding in format { pk: [shorturl, longurl] }
        # Increment the primary key for next url
        self.mappings[pk] = [suffix, longUrl]
        self.pk += 1
        
        return "http://tinyurl.com/" + suffix
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        # Extract the suffix from url
        suffix = shortUrl.split('/')[-1]
        
        # Decode the short url to a primary key
        pk = 0
        for i in range(len(suffix)):
            if 'a' <= suffix[i] <= 'z':
              pk = pk*62 + ord(suffix[i]) - ord('a')
            if 'A' <= suffix[i] <= 'Z':
              pk = pk*62 + ord(suffix[i]) - ord('A') + 26
            if '0' <= suffix[i] <= '9':
              pk = pk*62 + ord(suffix[i]) - ord('0') + 52
            
        # If this primary key is mapped, return the long url
        if pk in self.mappings:
            return self.mappings[pk][1]
        else:
            return None
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

#-------------------------------------------------------------------------------
