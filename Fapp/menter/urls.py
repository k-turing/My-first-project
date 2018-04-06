from django.conf.urls import url
from . import views

urlpatterns = [
#トップページ
url(r'^$', views.index, name = 'index'),
#メンター
url(r'^menter$', views.menter, name = 'menter'),
#コンタクト
url(r'^contact$', views.contact, name = 'contact'),
#コメント
url(r'^comment$', views.comment, name = 'comment'),
#アバウト
url(r'^about$', views.about, name = 'about'),
#哲学
url(r'^philosophy$', views.philosophy, name = 'philosophy'),
#ディテール
url(r'^([0-9]+)/$', views.detail, name='detail'),
#like
url(r'^([0-9]+)/like$', views.like, name='like'),
#デリート
#url(r'^([0-9]+)/delete$', views.delete, name='delete'),
#アップデート
#url(r'^([0-9]+)/update$', views.update, name='update'),

]
