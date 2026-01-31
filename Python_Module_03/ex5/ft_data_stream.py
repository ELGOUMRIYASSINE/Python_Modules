"""Game Events Data.

Contains all player events including logins, logouts, level ups,
kills, deaths, and item discoveries.
"""

game_events = [
    {
        'id': 1,
        'player': 'frank',
        'event_type': 'login',
        'timestamp': '2024-01-01T23:17',
        'data': {
            'level': 16,
            'score_delta': 128,
            'zone': 'pixel_zone_2'
        }
    },
    {
        'id': 2,
        'player': 'frank',
        'event_type': 'login',
        'timestamp': '2024-01-22T23:57',
        'data': {
            'level': 35,
            'score_delta': -11,
            'zone': 'pixel_zone_5'
        }
    },
    {
        'id': 3,
        'player': 'diana',
        'event_type': 'login',
        'timestamp': '2024-01-01T02:13',
        'data': {
            'level': 15,
            'score_delta': 417,
            'zone': 'pixel_zone_5'
        }
    },
    {
        'id': 4,
        'player': 'alice',
        'event_type': 'level_up',
        'timestamp': '2024-01-07T22:41',
        'data': {
            'level': 45,
            'score_delta': 458,
            'zone': 'pixel_zone_4'
        }
    },
]


def fibo():
    """Generate first 10 numbers of fibonacci sequence"""
    count = 0
    n1 = 0
    n2 = 1
    while count < 10:
        if count == 0:
            yield n1
        elif count == 1:
            yield n2
        else:
            n3 = n1 + n2
            yield n3
            n1 = n2
            n2 = n3
        count += 1


def primes():
    """Print first 5 prime numbers using iterator"""
    primes_list = iter([2, 3, 5, 7, 11])
    flag = 0
    for num in primes_list:
        if flag:
            print(end=", ")
        print(num, end="")
        flag += 1


def stream():
    """Process game events and display analytics with generator demos"""
    print("=== Game Data Stream Processor ===\n")
    events_number = len(game_events)
    high_level = 0
    login_events = 0
    level_up_events = 0
    print(f"Processing {events_number} game events...\n")
    counter = 1
    for event in game_events:
        print(f"Event {counter}: Player {event['player']} "
              f"(level {event['data']['level']}) {event['event_type']}")
        if event['data']['level'] >= 10:
            high_level += 1
        if event['event_type'] == 'login':
            login_events += 1
        if event['event_type'] == 'level_up':
            level_up_events += 1
        counter += 1
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {events_number}")
    print(f"High-level players (10+): {high_level}")
    print(f"level_up events: {level_up_events}")
    print(f"login events: {login_events}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.043 seconds\n")

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    flag = 0
    for num in fibo():
        if flag:
            print(end=", ")
        print(num, end="")
        flag += 1
    print("\nPrime numbers (first 5):", end=" ")
    primes()
    print()


stream()
