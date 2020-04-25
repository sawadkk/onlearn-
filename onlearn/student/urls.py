
from django.urls import path
from django.conf.urls import url
from . import views





urlpatterns = [
	path('',views.home,name = 'home'),
	url(r'^addcart(?P<a>\d+)',views.addcart,name='addcart'),
	path('cart',views.cartpage,name ='cart'),
	url(r'^buy(?P<a>\d+)',views.buy,name='buy'),
	path('mycourses',views.mycourse,name ='mycourses'),
	url(r'^cart_delete(?P<a>\d+)/$',views.cart_delete,name='cart_delete'),
	path('search',views.search,name ='search'),
	url(r'^addreview(?P<a>\d+)',views.addreview,name='addreview'),

]




