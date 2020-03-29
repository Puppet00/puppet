import datetime, requests, random
#Code By GogoZin
def CN_Proxy_Clone():
    print("\n\nChina Proxy Downloader")
    print("    CN_Proxy_Download    ")
    print("\nCode By Bossy\n\n")
    input("Press Any Key To Auto Get Http Proxies !\n")
    try:
        theTime = str(datetime.datetime.now())
        year = theTime.split("-")
        mon = year[1]
        day = year[2].split(" ")
        hour = day[1].split(":")
        url = "https://ip.ihuan.me/today/"+year[0]+"/"+mon+"/"+day[0]+"/"+str(hour[0])+".html" #Code By Bossy
        r = requests.get(url)
        html = str(r.text)
        html = html.split('</div>')
        html = html[6].split("</p>")
        html = html[0].split('<p class="text-left"> ')
        html = html[1]
        html = html.split("<br>")
        proxies = ""
        outputfile = open("proxies.txt","w")
        for proxy in html:
            proxy = proxy.split("@HTTP#")
            try:
                proxies = proxies + str(proxy[0])+"\n"
            except:
                pass
        outputfile.write(proxies)
        outputfile.close()
        num = len(open("proxies.txt").readlines())
        print("All Proxies Downloaded Total Proxies Count : "+str(num)+"\nSave As -> proxies.txt")
    except:
        print("Wait 10 minutes For New Proxies")
        quit()

if __name__=="__main__":
    CN_Proxy_Clone()
    #Code By Bossy
