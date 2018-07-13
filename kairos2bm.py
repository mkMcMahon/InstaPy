from instapy import InstaPy

session = InstaPy(username='vgnhphpmvmnt', password='gunston', headless_browser=True)
#session.set_use_clarifai(enabled=True, api_key='xxx')

session.login()

#session.like_by_tags(['water', ], amount=6, media=None)
#session.like_from_image([''], amount=, media=None)
#session.follow_user_followers([''], amount=, sleep_delay=, randomize=False, interact=False)
#session.follow_by_list([''], times=1)


# Like posts based on hashtags and like 3 posts of its poster
session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
# Interact with specific users
 #set_do_like, set_do_comment, set_do_follow are applicable

session.set_upper_follower_count(limit=30000)
session.set_lower_follower_count(limit = 1)

session.set_do_follow(enabled=False, percentage=0)
#session.set_comments(['⚡️💜😸💜 pic! @{}'], media='Photo')

#session.set_comments(['💞💛💜💓 video! @{}'], media='Video')
session.set_comments([u'☘️🍃🌾🌼 🌱' ,u'🌱 ☘️🍃🍄 🌱 ', u'🌵☘️🌴 🌱', u'🌸⚡️💜😸💜⚡️🌸', u'💜❤️💚💞💛💜💓💥💥💥', u'💞💞🙌💥💥👼💥', u'💚🌈💜🙏💚', u'😭🌈🌊💦💥💥💥💛💚🌈🌈🌈🌈💅🏾⚡️⚡️⚡️'])
session.set_do_comment(enabled=True, percentage=100)
session.set_do_like(False, percentage=000)



session.like_by_tags(['glassinthewild'], amount=100, interact=True)

#session.interact_by_users(['bobby_murugu'], amount=80, randomize=True, media="Photo")

session.end()
