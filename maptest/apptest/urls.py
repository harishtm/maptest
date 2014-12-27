from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^create_user/', 'apptest.views.create_user',name="create_user"),
    url(r'^list-all-user/', 'apptest.views.list_all_user',name="list_all_user"),
)
