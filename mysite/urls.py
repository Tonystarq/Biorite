"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import home
from home import views
from order import views as OrderViews
from user import views as UserViews
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),
    path('savelangcur', views.savelangcur, name='savelangcur'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    # path('jet/', include('jet.urls', 'jet')),
    path('currencies/', include('currencies.urls')),
    path(_('admin/'), admin.site.urls),
    path('', views.index, name='home'),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls'), name='user'),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path(_('about/'), views.aboutus, name='aboutus'),
    path(_('verify/'), views.verify, name='verify'),
    path(_('authenticate.html'), views.verify, name='verifyautheticate'),
    path(_('about.html'), views.aboutus, name='verifyabout'),
    path(_('bio-rite-whey.html'), views.shopnow, name='verifyshopnow'),
    path(_('bio-mass-gainer.html'), views.shopnow, name='verifyshop'),
    path(_('category_list/'), views.category_list, name='category_list'),
    path(_('blog/'), views.blog, name='blog'),
    path(_('contact/'), views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shopcart/', OrderViews.shopcart, name='shopcart'),
    path('login/', UserViews.login_form, name='login'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('signup/', UserViews.signup_form, name='signup'),
    path('verify/<auth_token>', UserViews.user_verify, name='verify'),
    path('faq/', views.faq, name='faq'),
    path('ourteam/', views.ourteam, name='ourteam'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('products.html', views.shopnow, name='shopnow'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('more/', views.more, name='more'),
    path('ShippingandDeliveryPolicies/', views.ShippingandDeliveryPolicies, name='ShippingandDeliveryPolicies'),
    path('TermsandConditions/', views.TermsandConditions, name='TermsandConditions'),
    path('Refund/', views.Refund, name='Refund'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('PrivacyPolicies/', views.PrivacyPolicies, name='PrivacyPolicies'),
    prefix_default_language=False,
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)