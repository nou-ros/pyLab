python decouple, admin-honeypot, django-session-timeout, 

========
Outline
========

WIP - Django E-Commerce Project 

Shout out to Rathan Kumar Udemy Instructor

Models: 

 --User--

Account - Custom user account (UserManager - MyAccountManager)
UserProfile - User profile (will be auto created.)

--Cart--
Cart - Information about cart
CartItem - Relation between Cart & Products. 

--Category-- 
Category - Product Categories.

--Order-- 

Payment - Payment model for third party and user transaction info(Instead of paypal used a auto id generator using uuid5)
Order - Customer's(User) billing information & Payment Relationship. 
OrderProduct - Customer(User), Order, Payment, and product relationship. 


--Prodcut--
Product - Complete product information model with category relationship 
Variation - Relation ship between product and variations.(size and color handled here. Also added a VariationManager).


--Review--
ReviewRating - Customer(User) review, on product relationship with rating.

--Gallery--
ProductGallery - Product and multiple product related images relationship.

Forms are handled with ModelForm
