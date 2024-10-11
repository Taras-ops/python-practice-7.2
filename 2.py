events = {
    'KSE party': {
        'date': '11.11.2024',
        'location': 'Kyiv',
        'attendees': [],
        'max_attendees': 2
    }
}


def register_attendee(event_name, attendee_name):
    if event_name in events and len(events[event_name]['attendees']) < events[event_name]['max_attendees']:
        events[event_name]['attendees'].append(attendee_name)


def unregister_attendee(event_name, attendee_name):
    if event_name in events:
        events[event_name]['attendees'].remove(attendee_name)


def get_event_details(event_name):
    print(events[event_name])


def list_all_events():
    for key, val in events.items():
        print(f'{key}: {val}')


register_attendee('KSE party', 'User')
print(events)

unregister_attendee('KSE party', 'User')
print(events)

get_event_details('KSE party')
list_all_events()