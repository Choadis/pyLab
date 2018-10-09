from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "Martin": {
        "name": 'Steve Martin',
        "age": 73,
        "occupation": 'comedian',
        "timestamp": get_timestamp()
    },
    "Depp": {
        "name": 'Johnny Depp',
        "age": 55,
        "occupation": 'actor',
        "timestamp": get_timestamp()
    },
    "Hagar": {
        "name": 'sammy Hagar',
        "age": 70,
        "occupation": 'musician',
        "timestamp": get_timestamp()
    },
    "Elvis": {
        "name": 'Elvis Presley',
        "age": 42,
        "occupation": 'musician',
        "timestamp": get_timestamp()
    },
    "Johnson": {
        "name": 'Joe Johnson',
        "age": 25,
        "occupation": 'driver',
        "timestamp": get_timestamp()
    },
    "Andrews": {
        "name": 'Sarah Andrews',
        "age": 31,
        "occupation": 'consultant',
        "timestamp": get_timestamp()
    },
    "Jackson": {
        "name": 'Samuel L Jackson',
        "age": 69,
        "occupation": 'actor',
        "timestamp": get_timestamp()
    },
    "Wozniak": {
        "name": 'Steve Wozniak',
        "age": 68,
        "occupation": 'programmer',
        "timestamp": get_timestamp()
    },
    "Lovelace": {
        "name": 'Ada Lovelace',
        "age": 36,
        "occupation": 'programmer',
        "timestamp": get_timestamp()
    },
    "Hopper": {
        "name": 'Grace Hopper',
        "age": 85,
        "occupation": 'programmer',
        "timestamp": get_timestamp()
    },
    "Turing": {
        "name": 'Alan Turing',
        "age": 41,
        "occupation": 'programmer',
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
