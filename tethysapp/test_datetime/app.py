from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.stores import PersistentStore

class TestDatetime(TethysAppBase):
    """
    Tethys app class for test datetime.
    """

    name = 'test datetime'
    index = 'test_datetime:home'
    icon = 'test_datetime/images/icon.gif'
    package = 'test_datetime'
    root_url = 'test-datetime'
    color = '#e67e22'
    description = ''
    tags = 'test'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='test-datetime',
                           controller='test_datetime.controllers.home'),
        )

        return url_maps

    def persistent_stores(self):
        """
        Add one or more persistent stores
        """
        stores = [PersistentStore(name='test_datetime_db_engine',
                                  initializer='test_datetime.init_stores.init_test_datetime_db',
                                  spatial=False
                                  )
                 ]

        return stores