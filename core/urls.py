from django.urls import path
from core.views import AESEncryptView, AESDecryptView, DESEncryptView, DESDecryptView, AESPageView, homepage, \
    DesPageView, RSAView, RSAKEYView, RSAEncrypt, RSADecrypt, DSAView, DSAKEYView, DSAEncryptView, DSADecryptView

urlpatterns = [
    path('', homepage),

    path('aes', AESPageView, name='aes-algorithm'),
    path('aes-encrypt', AESEncryptView, name='aes-encrypt'),
    path('aes-decrypt', AESDecryptView, name='aes-decrypt'),

    path('des', DesPageView, name='des-algorithm'),
    path('des-encrypt', DESEncryptView, name='des-encrypt'),
    path('des-decrypt', DESDecryptView, name='des-decrypt'),

    path('rsa', RSAView, name='rsa-algorithm'),
    path('rsa-key', RSAKEYView, name='rsa-key-gen'),
    path('rsa-encrypt', RSAEncrypt, name='rsa-encrypt'),
    path('rsa-decrypt', RSADecrypt, name='rsa-decrypt'),

    path('dsa', DSAView, name='dsa-algorithm'),
    path('dsa-key', DSAKEYView, name='dsa-key-gen'),
    path('dsa-encrypt', DSAEncryptView, name='dsa-encrypt'),
    path('dsa-decrypt', DSADecryptView, name='dsa-decrypt'),
]
