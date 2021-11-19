import os
import sys

token = os.environ.get("BOT_TOKEN")
prefix = os.environ.get("BOT_PREFIX")
DEFAULT_PREFIX = "!"

# if the token wasn't found as an env variable, try loading the credentials file
if not token or not prefix:
    try:
        import settings
    except:
        pass
    else:
        # env variables take priority, so only set an option if it's missing
        if not token:
            if hasattr(settings, "token"):
                token = settings.token
                
        if not prefix:
            if hasattr(settings, "prefix"):
                prefix = settings.prefix

# if the token is missing, we can't start
if not token:
    print("No token found! Please set a token in settings.py or")
    print("through an environment variable")
    sys.exit(1)
# if the prefix is what was missing, then simply default to a "!"
if not prefix:
    print("No prefix set! Configure a custom prefix in settings.py or")
    print("through an environment variable")
    print()
    print("Defaulting to prefix:", DEFAULT_PREFIX)
    prefix = DEFAULT_PREFIX
