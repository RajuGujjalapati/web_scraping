from requests_html import html
with open('simple.txt') as file:
    source=file.read()
    html_code=HTML(html=source)
    html_code.render()#this gives the dynamic data, which is located in javascriot
match=html.find('title',first=True)#gives the first element
    #if we want footer inforamtion
match=html.find('#footer',first=True)
#if we want first div and with some article name
atticles=html.find('div.class_name',first=True)
#if we remove the first=True , then it will print every div tag which has this
#class name.Now, if u want to extract id, para,h2,..tags use a for loop so that
#u will get everything
for match in articles:
headline=match.find('h2').text
summary=match.find('p').text

    print(match.text)

##analyzing data from web site
    from requests_html import html,HTMLSession
    r=HTMLSession()
    s=r.get('link')
    try:
    headline=article.find('.class_name').text
    summary=article.find('.class_name p').text#this gives data about para within thata class
    vid_src=aetcle.find('iframe'first=True)
    print(vid_src.attrs['src'])#this guves dictionary ['attributes']
    youtube_format=f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        #we can use pass if w dont want , but in this case we pass youtube_foramt=None, so it prints none when it reaches.
#if you are scraping pages some times if there is no youtube link then,use
    #try and exception block, if some variable is causing error put that naem
    #under the exception block and then put None , so we wont get error
#now if we want to save all darta into the csv file in the starting use
    import csv
    csv_file=open('some_file.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['headline','summary','video'])
    #at the bottom
    csv_writer.writerow([headline,summary,yt_format])
csv_file.close()


#if we want just links from a website use
s.html.links
#loop through above
for links in s.html.links:
    print(links)
#if we want more specific links :
    use
    for links in absolute_links:
        print(limks)

        


