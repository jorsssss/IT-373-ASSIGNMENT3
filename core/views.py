from django.shortcuts import render

# Hardcoded announcements)
ANNOUNCEMENTS = [
    {
        "id": 1,
        "title": "Welcome to Portal!",
        "content": "Welcome to the Portal! We’re excited to have you here and can’t wait for you to explore all the features and resources available. This portal is designed to make your learning experience easier and more engaging—so dive in, explore, and feel free to reach out if you need any help."
    },
    {
        "id": 2,
        "title": "World Teacher's Day!",
        "content": "Hey everyone! Just a heads-up that there will be no classes tomorrow in celebration of World Teachers' Day! Let’s take this chance to appreciate all the amazing teachers out there who work so hard for us every day—happy World Teachers' Day!"
    },
]

def home(request):
    return render(request, 'core/home.html')

def announcements_list(request):
    return render(request, 'core/list.html', {'announcements': ANNOUNCEMENTS})

def announcements_detail(request, id):
    # Find the announcement by ID (mimicking a DB lookup)
    announcement = next((a for a in ANNOUNCEMENTS if a["id"] == id), None)
    if not announcement:
        return render(request, 'core/detail.html', {'error': "Announcement not found."})
    return render(request, 'core/detail.html', {'announcement': announcement})
