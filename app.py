from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'college_gym_secret_2024'

# ── In-memory data store (no DB needed for demo) ──────────────────────────────
events = [
    {
        "id": 1,
        "title": "Annual Sports Day",
        "date": "2025-04-10",
        "time": "09:00",
        "venue": "Main Gymnasium",
        "category": "Competition",
        "description": "Annual inter-college sports competition featuring track & field, basketball, and volleyball.",
        "organizer": "Sports Committee",
        "capacity": 200,
        "registered": 142,
        "image_color": "#e63946"
    },
    {
        "id": 2,
        "title": "Yoga & Wellness Workshop",
        "date": "2025-03-28",
        "time": "07:00",
        "venue": "Fitness Studio A",
        "category": "Workshop",
        "description": "Morning yoga session open to all students. Improve flexibility, reduce stress, and boost mental clarity.",
        "organizer": "Health Club",
        "capacity": 40,
        "registered": 31,
        "image_color": "#2d6a4f"
    },
    {
        "id": 3,
        "title": "Basketball Tournament",
        "date": "2025-04-05",
        "time": "14:00",
        "venue": "Indoor Court",
        "category": "Tournament",
        "description": "3-on-3 basketball tournament open to all departments. Register your team of 4 (3 players + 1 substitute).",
        "organizer": "Basketball Club",
        "capacity": 80,
        "registered": 64,
        "image_color": "#f4a261"
    },
    {
        "id": 4,
        "title": "Strength & Conditioning Seminar",
        "date": "2025-04-15",
        "time": "11:00",
        "venue": "Weight Training Room",
        "category": "Seminar",
        "description": "Learn proper form, programming, and nutrition fundamentals from certified trainers.",
        "organizer": "Gym Faculty",
        "capacity": 50,
        "registered": 18,
        "image_color": "#457b9d"
    },
    {
        "id": 5,
        "title": "Zumba Dance Fitness",
        "date": "2025-03-30",
        "time": "17:00",
        "venue": "Aerobics Hall",
        "category": "Fitness",
        "description": "High-energy Zumba class combining Latin dance moves with cardio fitness. No experience needed!",
        "organizer": "Dance & Fitness Club",
        "capacity": 60,
        "registered": 55,
        "image_color": "#c77dff"
    },
    {
        "id": 6,
        "title": "Swimming Championship",
        "date": "2025-04-20",
        "time": "08:00",
        "venue": "Olympic Pool",
        "category": "Competition",
        "description": "Inter-department swimming championship across freestyle, backstroke, and relay categories.",
        "organizer": "Aquatics Club",
        "capacity": 100,
        "registered": 47,
        "image_color": "#00b4d8"
    },
]

registrations = []
next_event_id = 7

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    upcoming = sorted([e for e in events if e['date'] >= datetime.today().strftime('%Y-%m-%d')],
                      key=lambda x: x['date'])[:3]
    total_events = len(events)
    total_registered = sum(e['registered'] for e in events)
    return render_template('index.html', upcoming=upcoming,
                           total_events=total_events, total_registered=total_registered)

@app.route('/events')
def event_list():
    category = request.args.get('category', 'All')
    search = request.args.get('search', '').lower()
    filtered = events
    if category and category != 'All':
        filtered = [e for e in filtered if e['category'] == category]
    if search:
        filtered = [e for e in filtered if search in e['title'].lower() or search in e['description'].lower()]
    categories = ['All'] + sorted(set(e['category'] for e in events))
    return render_template('events.html', events=filtered, categories=categories,
                           selected_cat=category, search=search)

@app.route('/events/<int:event_id>')
def event_detail(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        flash('Event not found.', 'error')
        return redirect(url_for('event_list'))
    return render_template('event_detail.html', event=event)

@app.route('/events/<int:event_id>/register', methods=['POST'])
def register_event(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return jsonify({'success': False, 'message': 'Event not found'})
    name = request.form.get('name', '').strip()
    roll = request.form.get('roll', '').strip()
    dept = request.form.get('dept', '').strip()
    email = request.form.get('email', '').strip()
    if not all([name, roll, dept, email]):
        flash('Please fill all fields.', 'error')
        return redirect(url_for('event_detail', event_id=event_id))
    if event['registered'] >= event['capacity']:
        flash('Sorry, this event is full!', 'error')
        return redirect(url_for('event_detail', event_id=event_id))
    # Check duplicate
    already = any(r['event_id'] == event_id and r['roll'] == roll for r in registrations)
    if already:
        flash('You are already registered for this event!', 'warning')
        return redirect(url_for('event_detail', event_id=event_id))
    registrations.append({'event_id': event_id, 'name': name, 'roll': roll,
                          'dept': dept, 'email': email,
                          'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')})
    event['registered'] += 1
    flash(f'Successfully registered for {event["title"]}! 🎉', 'success')
    return redirect(url_for('event_detail', event_id=event_id))

@app.route('/admin')
def admin():
    return render_template('admin.html', events=events, registrations=registrations)

@app.route('/admin/add_event', methods=['POST'])
def add_event():
    global next_event_id
    colors = ['#e63946','#2d6a4f','#f4a261','#457b9d','#c77dff','#00b4d8','#e9c46a','#e76f51']
    new_event = {
        'id': next_event_id,
        'title': request.form.get('title'),
        'date': request.form.get('date'),
        'time': request.form.get('time'),
        'venue': request.form.get('venue'),
        'category': request.form.get('category'),
        'description': request.form.get('description'),
        'organizer': request.form.get('organizer'),
        'capacity': int(request.form.get('capacity', 50)),
        'registered': 0,
        'image_color': colors[next_event_id % len(colors)]
    }
    events.append(new_event)
    next_event_id += 1
    flash(f'Event "{new_event["title"]}" added successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    global events
    events = [e for e in events if e['id'] != event_id]
    flash('Event deleted.', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
