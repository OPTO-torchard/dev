## REST API

Representational State Transfer (REST)

You can make RESTful requests either on the device (localhost) or from elsewhere on the network, all you need is a request interface (a web browser or cUrl work too), the IP or hostname of your device, and of course the request URL and authentication key. The [_groov_ View REST API](http://developer.opto22.com/groov/view/ "Getting Started (developer.opto22.com)") and [_groov_ Manage REST API](http://developer.opto22.com/groov/manage/ "Getting Started (developer.opto22.com)") both support get and put/post requests, so it's possible to both read tags and I/O as well as write over tags and control outputs, depending on your application. The details of the request URL to access _groov_ View tags are in the [_groov_ View REST API Reference](http://developer.opto22.com/static/generated/groov-rest-api/swagger-ui/index.html?url=/static/generated/groov-rest-api/swagger.yaml "Swagger UI"), and _groov_ EPIC I/O requests are detailed in the  [_groov_ Manage REST API Reference](http://developer.opto22.com/static/generated/manage-rest-api/swagger-ui/index.html "Swagger UI")

If you want to execute RESTful programs to make requests from the EPIC processor itself you will need a shell license -- but you do not need one to RESTfully access the data from another device.

For basic REST API usage, you may want to check out our video on [How to Get & Post RESTful API Requests](https://www.youtube.com/watch?v=ypqiYtA6VtY& "OptoVideo") with the groov Edge Appliance and SNAP PAC Learning Center. Specifics on using the REST API with EPIC are covered in the [_groov_ Manage REST API documentation](http://developer.opto22.com/groov/manage/ "developer.opto22"), which can also be used through a browser, cUrl, application such as Postman, and languages like [Python](http://forums.opto22.com/t/epic-data-using-restful-python/2038 "forums.opto22").

[Top](#Top)


## Python for REST API

To make RESTful requests with Python requests you need to:

1. `sudo apt-get update`

    Do **NOT** apt-get upgrade!
2. `sudo apt-get install python-pip`

    Do **NOT** upgrade pip individually either!
3. `sudo pip install requests`

4. `import requests`

    Import the library to your script once it is installed

* Forum: [EPIC data using RESTful Python](http://forums.opto22.com/t/epic-data-using-restful-python/2038 "OptoForums")

* Developer: [groov Manage REST API](http://developer.opto22.com/groov/manage/ "developer.opto22.com")

[Top](#Top)