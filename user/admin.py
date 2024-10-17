from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


# ადმინიდან იუზერს ვერ დაამატებ რეალურად. არ მუშაობს. პაროლის ჰეშირებას არ აკეთებს.
# UserAdmin-საც ვარესტრირებდი მაგრამ გვიან ვნახე ერორი და დრო აღარ მეყო გასწორების.
# date_joined fieldზე აერორებდა რომელიც წავშალე და თავიდანაც გავუშვი მიგრაციები
# მაგრამ არ შველის.

# ესე იმიტომ დავტოვე რომ ერორზე არ გავიდეს და სხვა რაღაცები შემოწმებადი იყოს.
admin.site.register(User)