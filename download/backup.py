import requests
from .models import Version

def get_release_info():
    url = "https://api.github.com/repos/RedstoneCraftTeam/Redstone_Craft/releases"
    release_template_url = "https://github.com/RedstoneCraftTeam/Redstone_Craft/releases/tag/%s"
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.json()
    Version.objects.all().delete()

    for release in data:
        # Add \n at the end of each line in the description
        # Create or update the release object
        Version.objects.create(
            tag=release['tag_name'],
            title=release['name'],
            created_at=release['published_at'],
            description=release['body'],
            github_release=release_template_url % release['tag_name'],
            github_download_link=release['assets'][0]['browser_download_url'],
        )

if __name__ == '__main__':
    get_release_info()