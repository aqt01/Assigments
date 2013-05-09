
access_token_key = "73563424-GQ9p5GF8OMEkWKkkPzmV6auuenhbDfF8A97C6Bip0"
access_token_secret = "8umsUm6NUBVmXf2Lf8mJiauO7M7r2eDLymRYRsdzU"

consumer_key = "RsudjsH4QfQXeI3I0eG7Q"
consumer_secret = "Q2hM5fY4KrVQUZyvb1Ao8r2UeUMfHCErK2tAmmKcjU4"

_debug = 0

oauth_token = oauth.Token(key=access_token_token, secret=consumer_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

