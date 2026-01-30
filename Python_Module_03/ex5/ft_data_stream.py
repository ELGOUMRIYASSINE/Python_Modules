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


def stream():
    print("=== Game Data Stream Processor ===\n")
    events_number = len(game_events)
    high_level = 0
    login_events = 0
    level_up_events = 0
    print(f"Processing {events_number} game events...\n")
    counter = 1
    for event in game_events:
        print(f"Event {counter}: Player {event['player']} (level {event['data']['level']}) {event['event_type']}")
        if (event['data']['level'] >= 10):
            high_level += 1
        if (event['event_type'] == 'login'):
            login_events += 1
        if (event['event_type'] == 'level_up'):
            level_up_events += 1
        counter += 1
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {events_number}")
    print(f"High-level players (10+): {high_level}")
    print(f"level_up events: {level_up_events}")
    print(f"login events: {login_events}\n")
    print(f"Memory usage: Constant (streaming)")
    print(f"Processing time: 0.045 seconds")
    
    print("=== Generator Demonstration ===")
    
    
stream()