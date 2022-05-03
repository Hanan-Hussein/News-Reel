import unittest
from app.models import News_Source


class test_news_source(unittest.TestCase):
    """
    The test for the news_source class

    Args:
        unittest : The unittest
    """
    def setUp(self):
        """
        This is the set up that runs before the test
        """
        self.new_news_source = News_Source('BBC','www.news.com','this is a news source','KE','Swahili','Romantic',1)
        
    def test_news_source_(self):
        """
        Test if the instance created by news_source
        """
        self.assertTrue(isinstance(self.new_news_source,News_Source))
        
if __name__ == '__main__':
    unittest.main()