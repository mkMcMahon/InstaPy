from instapy import InstaPy

session = InstaPy(username='vgnhphpmvmnt', password='gunston')

session.login()

session.like_by_tags(['blacklivesmatter', 'blm', 'altonsterling'], amount=55, media=None)

session.end()