class Config(object):
    LOGGER = True
    API_ID = 2374504
    API_HASH = "2ea965cd0674f1663ec291313edcd333"
    TOKEN = "1710587682:AAFk3WOqWNZ4aqOSxclvc4ZqVhIW7pjgZnE"
    DB_URI = "postgres://ulfcpxkc:zqBMxEiu7VfwdMjnB2qpZEKySNsnBuhc@arjuna.db.elephantsql.com/ulfcpxkc"
    LOG_CHANNEL = -1001315521755 # if you want a logging channel you can add this, else logs will go into Owner's PM

class Development(Config):
    TEST_DEVELOP = True
    LOGGER = True
