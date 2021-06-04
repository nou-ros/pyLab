Simple django app to perform various admin dashboard operations. 

# Summernote 
Summernote rich text editor is used here. (https://github.com/summernote/django-summernote)

# Model relations:
- One to One(Blog and Blog settings) - one specific blog have one settings.
- One to Many(Blog and Comments) - A blog post can have many comments but one comment belongs to one specific blog post.

- Many to Many(Blogs and Tags) - A blog post can have many tags and a tag can belong to many blog posts. Category is used here for Tags. 

# to create 500 blog posts using faker
from faker import Faker
>>> faker = Faker()
>>> from blog.models import Blog
>>> for _ in range(0, 500):
>>>     Blog.objects.create(title=faker.sentence(), body=faker.paragraph())


# to create 3 comments for each blog post using faker
from faker import Faker
>>> faker = Faker()
>>> from blog.models import Blog, Comment
>>> for blog in Blog.object.iterator(): # iterator is better as it will load each blog at a time instead of loading all the data in the memory 
>>>     comments = [Comment(text=faker.paragraph(), blog=blog) for _ in range(0,3)]
>>>     Comment.objects.bulk_create(comments)


# Users: 

-> Non staffusers 
- is_staff = False and is_superuser=False
- Cannot access or login in the admin

-> Staff users
- is_staff=True and is_superuser=False
- can log in but cannot do anything until they're given permissions

-> Superusers
- is_staf=True and is_superuser=True
- Have all powers, can do anything even deleting themselves.

We can create group permission for set of users users

# Third Party app for admin
(styling)
- django-admin-list-filter-dropdown (https://github.com/mrts/django-admin-list-filter-dropdown)

- django-admin-rangefilter (https://github.com/silentsokolov/django-admin-rangefilter)

(export/import)
- export and import data from admin (https://django-import-export.readthedocs.io/en/latest/installation.html)

( Change Django admin interface.)
- change dashboard look in admin (https://django-grappelli.readthedocs.io/en/latest/)

- another package material admin (https://github.com/MaistrenkoAnton/django-material-admin)

for more check here(https://awesomeopensource.com/project/originalankur/awesome-django-admin)

otp based authentication.

django admin honeypot to secure admin (https://django-admin-honeypot.readthedocs.io/en/latest/) for fake admin login
