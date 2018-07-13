from instapy import InstaPy

session = InstaPy(username='vgnhphpmvmnt', password='gunston', headless_browser=True)
#session.set_use_clarifai(enabled=True, api_key='xxx')

session.login()

session.like_by_tags(['pulaski', ], amount=60, media=None)
#session.like_from_image([''], amount=, media=None)
#session.follow_user_followers(['waterfallwizard'], amount=100, sleep_delay=, randomize=False, interact=False)
#session.follow_by_list([''], times=1)

# Interact with specific users
 #set_do_like, set_do_comment, set_do_follow are applicable

session.set_upper_follower_count(limit=30000)
session.set_lower_follower_count(limit = 1)

session.set_do_follow(enabled=False, percentage=50)
session.set_comments([u'🌼 🌱' ,u'🌱  ', u'🌴 🌱', u'☘️🍃🌾', u'🌵☘️', u'🍃🍄', u'☘️ 🌱'])
session.set_do_comment(enabled=True, percentage=100)
session.set_do_like(False, percentage=100)
session.interact_by_users(['bobbymurugu'], amount=15, randomize=False, media="Photo")

session.end()
