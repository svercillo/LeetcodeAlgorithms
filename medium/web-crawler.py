# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        visited = set()

        def compare_host_names(site1, site2):
            host1 = site1.split("/")[2]
            host2 = site2.split("/")[2]
            return host1 == host2
            

        def dfs(url,res):
            nonlocal startUrl

        
            if url in visited:
                return

            visited.add(url)

            if not compare_host_names(url, startUrl):
                return 

            res.append(url)
            

            for new_url in htmlParser.getUrls(url):

                dfs(new_url, res)


        result = []

        dfs(startUrl, result)

        return result
