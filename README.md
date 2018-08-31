# URL Shortener
*- A Web Service using Python*

https://z-urlshortener.herokuapp.com/

## Summary

This web service has a POST /shorten_url endpoint that receives a JSON body with the URL to shorten. A successful request returns a JSON body with the shortened url.

<p align="left"> 
<img src = "images/Postman_01_Post.PNG" width=850">
</p>

A GET request made to the shortened URL redirects the user to the the original URL, or the contents of the original URL is returned.

<p align="left"> 
<img src = "images/Postman_02_Get.PNG" width=850">
</p>

Appropriate validation on the URL to be shortened is performed.

<p align="left"> 
<img src = "images/Postman_03_Url Validation.PNG" width=850">
</p>
                                                            
## Web Interface

The application is hosted on Heroku platform, and it has a web user interface.

<p align="left"> 
<img src = "images/Heroku_01_Home.PNG" width=850">
</p>
