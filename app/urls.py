from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("shop/",views.shop,name='shop'),
    path("shop/<int:post_id>",views.shopdet,name='shopdet'),
    path("shop/page/<int:page_id>",views.shop,name='shop_id'),
    path("like/<int:ido>",views.like,name='like'),
    path("cart/",views.profile,name='prof'),
    path("us/",views.us,name='us'),
    path("checkout/",views.checkout,name='checkout'),
    path("signup/",views.signup,name='signup'),
    path("signin/",views.signin,name='signin'),
    path("logout/",views.logout,name='logout'),
    path("blog/",views.coming,name="co"),
]
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)