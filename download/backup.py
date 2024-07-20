import requests
from .models import Version, Backup

def get_release_info():
    url = "https://api.github.com/repos/RedstoneCraftTeam/Redstone_Craft/releases"
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.json()
    if data is None:
        return
    if Backup.objects.count() > 0 and data == Backup.objects.last().api_response:
        return
    Version.objects.all().delete()

    for release in data:
        # Add \n at the end of each line in the description
        # Create or update the release object
        Version.objects.create(
            tag=release['tag_name'],
            title=release['name'],
            created_at=release['published_at'],
            description=release['body'],
            github_release=release['html_url'],
            github_download_link=release['assets'][0]['browser_download_url'],
        )
    
    return response.text

if __name__ == '__main__':
    get_release_info()