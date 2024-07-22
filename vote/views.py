from django.shortcuts import render
from models import Vote
# Create your views here.
def vote_page(request, vote_name):
    """
    By gene-2012
    """
    vote_obj = Vote.objects.get(name=vote_name)
    vote_vts = vote_obj.vts_file.read().decode('utf-8')
    render(request, 'voteInfo.html', {'vote_obj' : vote_obj, 'vote_vts' : vote_vts})