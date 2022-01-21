import random

when = ['A long time ago', 'Yesterday',
        'A few years ago', 'Last night', 'On 15th September']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Mog', 'Ele', 'Ota', 'Shag', 'Soe', 'Tim']
residance = ['Barcelona', 'Canada', 'Germany', 'Bangladesh', 'Russia', 'Japan']
went = ['cinema', 'university', 'seminar', 'school', 'kitchen']
happend = ['made a lot of friends', 'jumped happily',
           'found a secret key', 'solved a mistery', 'wrote a book']


print(random.choice(when) + ", " + random.choice(who) + " that lived in " +
      random.choice(residance) + ", went to the  " + random.choice(went) + " and " + random.choice(happend) + ".")
