#----
#OK
#----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# test for tweeter get elements
# **********x*****************************
# loag all pages
from selenium import webdriver

chromedriver = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(executable_path=chromedriver,options=options);
driver.get("https://twitter.com/explore")
time.sleep(5)

driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[1]/div/div/div[1]/a/div/span/span').click()
while(True):
    try:

        # driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys('mehregan_ghobakhloo@yahoo.com')
        # driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys('123456789m')
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys('sirpostchirr@gmail.com')
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys('rezvanrr2001')
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span').click()

        break
    except:
        continue

time.sleep(4)


list_searched=['#وام_مسکن',
               '#وام_ازدواج',
                '#وام_خودرو',
                '#وام_تعمیرات',
                '#انواع_سپرده',
               ];
from selenium.webdriver.common.keys import Keys
for searchKey in list_searched:
    # searchKey='#وام_ازدواج'

    URLS=[]
    while(True):
        try:

            driver.get("https://twitter.com/search?q=%23" + searchKey.replace('#', '') + "&src=typed_query")

            time.sleep(5)
            break
        except:
            time.sleep(3)
            continue

    # Get all  URL of posts  (hrefs)

    # Get all POsts
    list_allPost=[]
    for x in range(0, 10):
        # all_post=driver.find_elements_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div/div/article/div/div[2]/div[2]/div[1]/div[1]/a")

        all_post=driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div")



        for po in all_post:
            # cnt_try=0
            while(True):
                try:
                    # '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[5]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a'
                    po_attribute=po.find_element_by_xpath('div/div/div/div/article/div/div[2]/div[2]/div[1]/div/div/div[1]/a')


                    href=po_attribute.get_attribute("href")
                    if (href not in list_allPost):
                        list_allPost.append(href)
                    break
                except:
                    try:
                        po_attribute = po.find_element_by_xpath(
                            'div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a')
                        href = po_attribute.get_attribute("href")
                        if (href not in list_allPost):
                            list_allPost.append(href)
                        break
                    except:
                        time.sleep(1)
                        break


        driver.execute_script(
            "window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));");
        time.sleep(3)
    #
    cnt_post=0
    for postURL in list_allPost:
        driver.get(postURL)
        time.sleep(5)

        #---------------
        # Get Author Information
        #--------------------
        while(True):
            try:


                # post=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]/div').text

                # '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div/div[1]/div/div/article/div/div/div/div[3]/div[1]/div[1]'
                # post=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]/div/span[3]').text
                # post=driver.find_element_by_class_name('div[@class="css-1dbjc4n"]').text
                Element=driver.find_element_by_class_name('css-1dbjc4n').text
                post=Element
                author='@'+Element.split('@')[1].split('\n')[0]
                # author=driver.find_element_by_class_name("css-1dbjc4n").text
                # '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > section > div > div > div > div:nth-child(1) > div > div > article > div > div > div > div:nth-child(3) > div.css-1dbjc4n.r-156q2ks'
                # author = driver.find_element_by_xpath(
                #     "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]/div/span").text
                break
            except:
                continue

        print('post_'+str(cnt_post)+'_Autor==='+author)
        #-----------------------
        #get userLikes
        # -----------------------
        list_users=list()
        str_userLikes = ""
        cnt_try_like=0
        try:
            #------------------
            while(True):
                try:
                    links_userLikes=postURL+'/likes'
                    # links_userLikes=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[4]/div[2]/div/a').get_attribute("href")
                    # links_userLikes=driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]')
                    # link_likesUsers=links_userLikes[0].find_element_by_xpath('div[3]/div/div/a').get_attribute("href")

                    break
                except:
                    try:
                        link_likesUsers = links_userLikes[0].find_element_by_xpath('div[4]/div[2]/div/a').get_attribute(
                            "href")


                    except:
                        print('-')

                    cnt_try_like=cnt_try_like+1
                    if (cnt_try_like==4):
                        break
                    time.sleep(1)
                    continue
            # ------------------

            driver.execute_script("window.open('','_blank');")
            driver.switch_to_window(driver.window_handles[1])  # assuming new tab is at index 1
            driver.get(links_userLikes)
            time.sleep(4)
            tedad=5
            while(True):
                while(True):
                    try:
                        list_users = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/div/section/div/div/div/div')
                        break
                    except:
                        continue

                if (len(list_users)==0):
                    time.sleep(1)
                    tedad=tedad-1
                    if (tedad==0):
                        break
                    continue
                break;
            list_userLikes=[]
            for ustLikes in list_users:
                ustLikes_text=ustLikes.find_element_by_xpath('div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div/span').text
                list_userLikes.append(ustLikes_text)
                str_userLikes=str_userLikes+ustLikes_text+" ";

            driver.execute_script("window.close('');")
            driver.switch_to_window(driver.window_handles[0])

        except:
            print("No like")
            try:
                driver.execute_script("window.close('');")
                driver.switch_to_window(driver.window_handles[0])
            except:
                print('-')

        print('post_'+str(cnt_post)+'_CountLikes==='+str(len(list_users)))

        #-------------------------
        #get userRetweets
        #--------------------------
        list_users=list()
        str_userRetweet = ""
        cnt_try_retweet=0
        try:
            #------------------
            while(True):
                try:

                    # link_RetweetUsers=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[4]/div[1]/div/a').get_attribute("href")
                    link_RetweetUsers=postURL+'/retweets'
                    break
                except:
                    cnt_try_retweet=cnt_try_retweet+1
                    if (cnt_try_retweet==4):
                        break
                    time.sleep(1)
                    continue

            #-----------------



            driver.execute_script("window.open('','_blank');")
            driver.switch_to_window(driver.window_handles[1])  # assuming new tab is at index 1
            driver.get(link_RetweetUsers)
            time.sleep(4)
            tedad = 5
            while(True):
                while(True):
                    try:
                        # '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]'
                        # '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/section/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]'
                        # '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div[2]/div[2]'
                        list_users = driver.find_elements_by_xpath(
                            '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/section/div/div/div/div')
                        break
                    except:
                        continue

                if (len(list_users)==0):
                    time.sleep(1)
                    tedad =tedad-1
                    if (tedad==0):
                        break
                    continue
                break;

            # list_users=driver.find_elements_by_xpath("div/div/div/div[2]/div[1]/div[1]/a/div/div[2]")
            list_userRetweet=[]

            for ustLikes_item in list_users:
                ustLikes=ustLikes_item.find_element_by_xpath('div/div/div/div[2]/div[1]/div[1]/a/div/div[2]')
                list_userRetweet.append(ustLikes.text)
                str_userRetweet=str_userRetweet+ustLikes.text+" "
            driver.execute_script("window.close('');")
            driver.switch_to_window(driver.window_handles[0])

        except:
            print("No Retweet")

        print('post_'+str(cnt_post)+'_CountRetweets==='+str(len(list_users)))

        #get UserComment
        # try:
        #     link_likesUsers=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div/div/div[2]/div/section/div/div/div/div[1]/div/article/div/div[5]/div[2]/a").get_attribute("href")
        #     driver.execute_script("window.open('','_blank') ;")
        #     driver.switch_to_window(driver.window_handles[1])  # assuming new tab is at index 1
        #     driver.get(link_likesUsers)
        #     time.sleep(4)
        #     # list_users_Items=driver.find_elements_by_xpath("//*[@id='react-root']/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/section/div/div/div/div")
        #     list_users=driver.find_elements_by_xpath("//*[@id='react-root']/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/section/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div/span")
        #     list_userLikes=[]
        #     for ustLikes in list_users:
        #         list_userLikes.append(ustLikes.text)
        #     driver.execute_script("window.close('');")
        #     driver.switch_to_window(driver.window_handles[0])
        #
        # except:
        #     print("No like")

        # driver.back()
        print('tamammmm_step_')
        driver.get("https://twitter.com/search?q=%23" + searchKey.replace('#', '') + "&src=typed_query")
        cc = driver.find_elements_by_xpath(
            "//*[@id='react-root']/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div")
        fpp = open(searchKey.replace('#', '') + '.txt', 'a', encoding='utf8')
        fpp.write("POST: "+post.replace('\n',' ')+'\n'+
                  "Autor: "+author.replace('\n',' ')+'\n'+
                  "UserLikes: "+str_userLikes.replace('\n',' ')+'\n'+
                  "UserRetweets: "+str_userRetweet.replace('\n',' ')+'\n'+
                  "----------------------------------------------------"+'\n')
        fpp.close()

            #-----------------------

