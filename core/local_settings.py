ALLOWED_HOSTS = ['192.168.99.100','127.0.0.1',]
SECRET_KEY="fd389fcc60bdf0670c2bf2ce9be721f8b57bdf2d52cc47c8"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'capes',
        'USER': 'postgres',
        'PASSWORD': '@1234567',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
