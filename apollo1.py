from instapy import InstaPy
from proxy_extension import create_proxy_extension

proxy = 'bwatso01:P0gtTVmC@172.241.37.18:29842'
proxy_chrome_extension = create_proxy_extension(proxy)

InstaPy(username='vgnhphpmvmnt', password='gunston',headless_browser=False,  proxy_chrome_extension='proxy_chrome_extension', nogui=True)\
    .login() \
    .set_do_comment(True, percentage=10) \
    .set_comments(['Cool!', 'Awesome!', 'Nice!']) \
    .set_dont_include(['khaverty7', 'bobbymurugu', 'mkmcmhn']) \
    .set_dont_like(['food', 'girl', 'hot']) \
    .like_by_tags(['dog', '#cat'], amount=2) \
    .end()
