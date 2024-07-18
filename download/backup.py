import requests
from .models import Version

def get_release_info():
    url = "https://api.github.com/repos/RedstoneCraftTeam/Redstone_Craft/releases"
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.json()

    for release in data:
        # Create or update the release object
        Version.objects.update_or_create(
            github_release=release['url'],
            defaults={
                'tag': release['tag_name'],
                'title': release['name'],
                'created_at': release['published_at'],
                'description': release['body']
            }
        )

if __name__ == '__main__':
    get_release_info()