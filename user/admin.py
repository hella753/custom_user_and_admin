from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

# ეს ერრორი მქონდა ამიტომ უბრალოდ ვარეგისტრირებდი რადგან გასასწორებლად არ დაერორებინა სხვა რაღაცებზე
# admin.site.register(User)
# ადმინიდან იუზერს ვერ დაამატებ რეალურად. არ მუშაობს. პაროლის ჰეშირებას არ აკეთებს.
# UserAdmin-საც ვარესტრირებდი მაგრამ გვიან ვნახე ერორი და დრო აღარ მეყო გასწორების.
# date_joined fieldზე აერორებდა რომელიც წავშალე და თავიდანაც გავუშვი მიგრაციები
# მაგრამ არ შველის.

# თუმცა დედლაინის შემდეგ გვიან გავასწორე და მუშაობს (staff1@gmail.com-ის პაროლი testi1234-ია)
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    list_per_page = 10
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff' ), }),)