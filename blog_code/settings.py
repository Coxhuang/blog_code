"""
Django settings for blog_code project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime
from blog_code.config import myconfig

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '00+99df#cjy1dr5u)c9_st_)a%1*m)4@f1%n*dn91@&%-ykfgh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = myconfig.DEBUG
# DEBUG = True

ALLOWED_HOSTS = ["*",]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_swagger',
    'django_filters',
    'django_crontab',
    'rest_framework.authtoken',
    'rest_framework',
    'app',
    'app_user',
    'app_test',
    'app_article', # 按照app创建的先后循序添加
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.common.middlewares.system.middleware.MySystemMiddleware', # 我的自定义系统异常
]

ROOT_URLCONF = 'blog_code.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog_code.wsgi.application'
AUTH_USER_MODEL = 'app_user.UserProfile'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CONN_MAX_AGE': 600,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
# USE_TZ = True


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 配置 MEDIA_ROOT 作为你上传文件在服务器中的基本路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') # 注意此处不要写成列表或元组的形式
# 配置 MEDIA_URL 作为公用 URL，指向上传文件的基本路径
MEDIA_URL = '/media/'
# 这里特意写成 upload 和 media，而不是统一写成 media 或 upload，是为了便于理解 MEDIA_ROOT 和 MEDIA_URL 的作用和区别

UPLOAD_IMAGES_BASE_PATH = "127.0.0.1:19900"

REST_FRAMEWORK = {
    "DEFAULT_VERSION": 'v1',  # 默认的版本
    "ALLOWED_VERSIONS": ['v1', 'v2'],  # 允许的版本
    "VERSION_PARAM": 'version',  # GET方式url中参数的名字  ?version=xxx
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', # 浏览器模式
    ),
    'EXCEPTION_HANDLER': 'app.utils.common.exceptions.exception.custom_exception_handler',

    'DEFAULT_THROTTLE_CLASSES': (
        # 'rest_framework.throttling.AnonRateThrottle',
        # 'rest_framework.throttling.UserRateThrottle'
        'rest_framework.throttling.ScopedRateThrottle',  # throttle_scope = 'uploads'
    ),
    'DEFAULT_THROTTLE_RATES': {
        # 'anon': '2/m',
        # 'user': '5/m',
        "throttle_base_30_Min": "30/m",  # 所有接口
        'login_throttle': '20/m', # 登录节流
    },
}

JWT_AUTH = {
    # 指明token的有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_ISSUER': 'http://fasfdas.baicu',
    'JWT_AUTH_HEADER_PREFIX': 'TOKEN',
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1)
}

# from django.contrib.auth import authenticate # 验证使用
AUTHENTICATION_BACKENDS = (
    'app.utils.common.authenticates.authenticate.CustomBackend',
)


# **********************************************************
# ********************** 全局常量  **************************
# **********************************************************
MY_PAGE_SIZE = 20 # 默认分页,每页显示条数
MY_ARTICLE_PAGE_SIZE = 5 # 客户端文章列表分页,每页显示条数
MY_PAGE_SIZE_QUERY_PARAM = "size" # 可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
MY_MAX_PAGE_SIZE = 1000 # 最大页数不超过1000
MY_PAGE_QUERY_PARAM = "page"  # 获取页码数的


"""
------------------------  跨域 Config ------------------------
"""
# 中间件
# 'corsheaders.middleware.CorsMiddleware', # 跨域
# 'django.middleware.common.CommonMiddleware', # 顺序不能变
# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    # 'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'User-agent',
    'x-csrftoken',
    'x-requested-with',
    'token',
)


FONTPATH = myconfig.FONTPATH # 系统字体

# celery config
CELERY_BROKER_URL = myconfig.get_celery_config()["CELERY_BROKER_URL"] # redis作为中间件
CELERY_ACCEPT_CONTENT = myconfig.get_celery_config()["CELERY_ACCEPT_CONTENT"]
CELERY_TASK_SERIALIZER = myconfig.get_celery_config()["CELERY_TASK_SERIALIZER"]
CELERY_RESULT_BACKEND = myconfig.get_celery_config()["CELERY_RESULT_BACKEND"] # 数据结果存储地址
CELERY_BEAT_SCHEDULE = myconfig.get_celery_config()["CELERY_BEAT_SCHEDULE"]
CELERY_TIMEZONE = myconfig.get_celery_config()["CELERY_TIMEZONE"] # 时区
