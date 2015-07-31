'''
This module contains the sampling util functions
'''

# from __future__ import unicode_literals
import request
import numpy as np

def get_sample(users, takes=10000):
    '''
    Get samples from random distribution
    '''
    samples = np.random.rand(5)
    size = len(users)
    return [users[int(samples[idx]*size)] for idx in range(1, takes)]

def getuser(idx):
    pageidx = int(idx/100)
    lineidx = int(idx%100)
    page = open('data/page_%i.txt'%(pageidx+1), 'r')
    line = page.readlines()[lineidx]
    user = line[5:].split(',')[0]
    page.close()
    return user

def cleanuser(userdata):
    cleaneddata = {}
    for key,val in userdata.iteritems():
        if not '_url' in key:
            cleaneddata[key] = val
    return cleaneddata
def get_users(users, agent):
    '''
    The agent shall be the request agent
    '''
    return [agent.get_user(user) for user in users]

def get_followers(users, agent):
    '''
    Get followers from the request agent
    '''
    followerlist = [[f['login'] for f in agent.get_followers(user)] for user in users]
    emptystr = ''
    maxlen = max(map(followerlist, len))
    for followers in followerlist:
        followers.extend(['']*(maxlen-len(followers)))
    return np.array([np.array(followers) for followers in followerlist])

 
