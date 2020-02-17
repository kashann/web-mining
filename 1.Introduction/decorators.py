from functools import wraps

def logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('i am called')
        return f(*args, **kwargs)
    return wrapper

@logger
def say(something):
    """
    i am a function (documentation)
    """
    print('saying ' + something)

def main():
    say('i am here')

if __name__ == '__main__':
    main()