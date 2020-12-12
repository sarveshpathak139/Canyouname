from flask import Flask, render_template, request
import requests
import time


   # import flask
app = Flask(__name__)            


@app.route("/")                
def hello():                   
    return render_template('index.html')    

@app.route("/result", methods = ['POST' , 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['name']

       
       
        # INSTAGRAM
        instagram = 'https://www.instagram.com/'+str(result)

        # FACEBOOK
        facebook = 'https://www.facebook.com/'+str(result)

        #TWITTER
        twitter = 'https://www.twitter.com/'+str(result)

        # YOUTUBE
        youtube = 'https://www.youtube.com/'+str(result)

        # BLOGGER
        blogger = 'https://'+str(result)+'.blogspot.com'


        # REDDIT
        reddit = 'https://www.reddit.com/user/'+str(result)

        # WORDPRESS
        wordpress = 'https://'+str(result)+'.wordpress.com'

        # PINTEREST
        pinterest = 'https://www.pinterest.com/'+str(result)

        # GITHUB
        github = 'https://www.github.com/'+str(result)

        # TUMBLR
        tumblr = 'https://'+str(result)+'.tumblr.com'


        # STEAM
        steam = 'https://steamcommunity.com/id/'+str(result)

        # VIMEO
        vimeo = 'https://vimeo.com/'+str(result)

        # SOUNDCLOUD
        soundcloud = 'https://soundcloud.com/'+str(result)


        # MEDIUM
        medium = 'https://medium.com/@'+str(result)

        # FLIPBOARD
        flipboard = 'https://flipboard.com/@'+str(result)

        # SLIDESHARE
        slideshare = 'https://slideshare.net/'+str(result)

        # SPOTIFY
        spotify = 'https://open.spotify.com/user/'+str(result)


        # WIKIPEDIA
        wikipedia = 'https://www.wikipedia.org/wiki/User:'+str(result)


        # IFTTT
        ifttt = 'https://www.ifttt.com/p/'+str(result)

        # EBAY
        ebay = 'https://www.ebay.com/usr/'+str(result)

        # SLACK
        slack = 'https://'+str(result)+'.slack.com'

        # OKCUPID
        okcupid = 'https://www.okcupid.com/profile/'+str(result)


        ''' WEBSITE LIST - USE FOR SEARCHING OF result '''
        WEBSITES = [
        instagram, facebook, twitter, youtube, blogger, reddit,
        wordpress, pinterest, github, tumblr, steam, vimeo, soundcloud, 
        medium,  flipboard, slideshare, spotify,
        wikipedia,  ifttt, ebay, slack, okcupid
        ]

        GREEN = outer_func('\033[92m')
        YELLOW = outer_func('\033[93m')

        RED = outer_func('\033[91m')


        count = 0
        match = True
        list1 = []
        list2 = []
        for url in WEBSITES:
            r = requests.get(url)

            if r.status_code == 200:

            
                if match == True:
                    GREEN('[+] FOUND MATCHES')
                    match = False
                YELLOW('\n'+url + '-' + str(r.status_code) + '- OK')
                print(type(result))
                print(type(r.text))
                if str(result) in r.text:
                    list1.append([url, "Found"])
                    GREEN('POSITIVE MATCH: result:'+str(result)+' - text has been detected in url.')
                else:
                    list2.append([url, "Not Found"])
                    GREEN('POSITIVE MATCH: result:'+str(result)+' - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')#
            else:
                list2.append([url, "Not Found"])
            count += 1


        total = len(WEBSITES)
        GREEN('FINISHED: A total of '+str(count)+' MATCHES found out of '+str(total)+' websites.')



        list3 = list1+list2
        print(list3)
        return render_template('result.html',result = list3)   


''' COLOUR PRINTING FUNCTION '''
def outer_func(colour):
    def inner_function(msg):
        print(colour+msg)
    return inner_function

    
if __name__ == "__main__":        
    app.run()                     