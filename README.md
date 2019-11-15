Rest API for blog platform where you can list blogs with and without their post, tags and comments. According to my model schema, what i call 'blog' is the thing when you write about a topic and send it. Post is its main content. I used Django, Django Rest Framework(drf) and Django Filter.The API also has a gui which makes understanding the project easy.


Why there is a way to list blogs with and without posts ? Because there are scenerios where you will only need to represent the title ( i named it 'header' on model schema) and do some stuff according to their authors or dates etc. 


Let's say, a mobile application is using this API. The app would probably have a main page for listing blogs and filtering mechanism according to author/date/topic. If we send the posts which the app dont use, it would cost much data and battery for the user. Bad reputation for the app.


Why I used SqLite ? Because it doesnt require any installation and easy to test for people to clone this project and try it out on their own computers.


So basically The API has 4 main links :
- /blogs/blogs/      => Listing blogs with posts. To add/update/delete blogs, this link is going to be used.
- /blogs/tags/       => Tags for our blogs like "History, Technology, Literature" etc.
- /blogs/bloglist/   => Listing blogs without posts. Read-only. No add/update/delete.
- /blogs/comments/   => Lists comments that left under all the blogs.


Another important think about this project is, on python code I followed underscore_naming culture as Python developers do and camelCase on json responses as JavaScript developers do. This caused a little trouble and broke the automation of drf and django-filter a little. Life would be much easier if I would use the same naming style but I guess I like fantasy :)


Since this is not a public API of a useful website like Instagram or Youtube, I am not going to explain everything in detail,because it is basically just how you use drf and django-filter. Instead, i will give couple of examples. Also, gui of the API is revealing for using django-filter if you do not know how to use.


---
### EXAMPLE-1
List blogs without posts that has 'Trip' tag (assume tag is is 7) :


request with 'GET' method to => /blogs/bloglist/?tagId__iexact=7 


possible response :
```javascript
[
    {
        "id": 3,
        "header": "My Trip to Bali",
        "author": "everybody_walking",
        "tagId": 7,
        "createDate": "2019-01-31T14:30:11.695224+03:00"
    },
    {
        "id": 4,
        "header": "Things You Should Know About Japan",
        "author": "tomonjushima",
        "tagId": 7,
        "createDate": "2019-01-31T14:31:37.764162+03:00"
    }
]
```
---
### EXAMPLE-2
Leave a comment under the "Story of Django Reinhardt" blog (assume blog id is 5) :


request with 'POST' method to => /blogs/comments/
with data :
```javascript
{
  "text": "I didn't know Django framework is named after him!",
  "author": "itisjustme",
  "authorEmail": "me@who.com",
  "blogId": 5,
}
```


possible response :
```javascript
{
  "id": 5,
  "text": "I didn't know Django framework is named after him!",
  "author": "itisjustme",
  "authorEmail": "me@who.com",
  "blogId": 5,
  "createDate": "2019-02-01T01:20:00.564896+03:00"
}
```
---
### EXAMPLE-3
Change the given blog's tag id to 1 (this is partial update): 


blog:
```javascript
{
    "id": 8,
    "header": "Where Are Aliens ? Are We Alone",
    "author": "everybody_walking",
    "tagId": 7,
    "createDate": "2019-01-31T14:30:11.695224+03:00"
}

```


request with "PATCH" method to => /blog/blogs/8/


with this data:
```javascript
{
    "tagId": 1
}
```


respone will be:
```javascript
{
    "id": 8,
    "header": "Where Are Aliens ? Are We Alone",
    "author": "everybody_walking",
    "tagId": 1,
    "createDate": "2019-01-31T14:30:11.695224+03:00"
}
```


Explanation: On this example we did partial update. But normal update happens with "PUT" http method and it requires all the not_null fields to be sent again even if we do not change them. id and createDate are read-only fields since they are automatically generated so If we would use PUT method on this example , we would have to send all the fields except id and createDate fields. Otherwise we would have error message.

**END OF EXAMPLES**
---