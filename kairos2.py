from instapy import InstaPy

InstaPy(username='vgnhphpmvmnt', password='gunston',headless_browser=False,  proxy_chrome_extension='proxy_chrome_extension', )\
#session.set_use_clarifai(enabled=True, api_key='xxx')

proxy = 'bwatso01:P0gtTVmC@172.241.37.18:29842'
proxy_chrome_extension = create_proxy_extension(proxy)

session.login()

#session.like_by_tags(['water', ], amount=6, media=None)
#session.like_from_image([''], amount=, media=None)
#session.follow_user_followers([''], amount=, sleep_delay=, randomize=False, interact=False)
#session.follow_by_list([''], times=1)

# Interact with specific users
 #set_do_like, set_do_comment, set_do_follow are applicable

session.set_upper_follower_count(limit=300000000)
session.set_lower_follower_count(limit = 1)

session.set_do_follow(enabled=False, percentage=50)
session.set_comments(['Nice pic! @{}'], media='Photo')
session.set_comments(['Nice video! @{}'], media='Video')
session.set_comments([u'☘️🍃🌾🌼 🌱' ,u'🌱 ☘️🍃🍄 🌱 ', u'🌵☘️🌴 🌱'])
session.set_do_comment(enabled=True, percentage=100)
session.set_do_like(False, percentage=100)
session.interact_by_users(['edgarfabianfrias'], amount=30, randomize=False, media="Photo")

session.end()
