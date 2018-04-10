from instapy import InstaPy

session = InstaPy(username='vgnhphpmvmnt', password='gunston', headless_browser=True)
#session.set_use_clarifai(enabled=True, api_key='xxx')

session.login()

session.like_by_tags(['water', 'running', 'exercise'], amount=6, media=None)
#session.like_from_image([''], amount=, media=None)
#session.follow_user_followers([''], amount=, sleep_delay=, randomize=False, interact=False)
#session.follow_by_list([''], times=1)

session.end()
