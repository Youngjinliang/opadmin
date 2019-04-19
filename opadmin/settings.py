"""
Django settings for opadmin project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u7uz2g-oyn-5b9v&9-#^o6)ar6ynm((&)!ji_evm(a_944j%r_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#LDAP config
import ldap
from django_auth_ldap.config import LDAPSearch,LDAPSearchUnion,PosixGroupType
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}
AUTH_LDAP_SERVER_URI = "ldap://192.168.56.101"
AUTH_LDAP_BIND_DN = "cn=Manager,dc=jcwit,dc=com"
AUTH_LDAP_BIND_PASSWORD = 'abc12345'
base_dn = 'ou=it,dc=jcwit,dc=com'
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=it,dc=jcwit,dc=com',ldap.SCOPE_SUBTREE,"(uid=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch('ou=group,dc=jcwit,dc=com',ldap.SCOPE_SUBTREE, '(objectClass=groupOfNames)',)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name":"givenName",
    "last_name":"sn",
    "email":"mail",
    "name":'cn',
    "mobile":"mobile",
}
AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'asset',
    'users',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'channels',
    'webterminal',
    'elfinder',
    'workplan',
    'xadmin',
    'crispy_forms',
    'reversion',
    'pure_pagination',
    'DjangoUeditor',
    'wiki',
    'ansible_task',
    'db_operation',
    'django_celery_results',
    'django_celery_beat',


]

#分页配置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10, #显示多少page页
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True, #页码不存在跳到首页
}
#跨域访问安装django-cors—headers，并配置MIDDLEWARE
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = "users.UserProfile"

AUTHENTICATION_BACKENDS = (
    #如果启用ldap认证无法使用企业微信认证
    #'django_auth_ldap.backend.LDAPBackend',
    'users.views.CustomBackend',

)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middlewares.rbac.RbacMiddleware',
]

ROOT_URLCONF = 'opadmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #  添加图片处理器：为了在列表中前面加上MEDIA_URL
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'opadmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ops',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 业务中的用户表
RBAC_USER_MODLE_CLASS = "users.models.UserProfile"
# 权限url数据
PERMISSION_SESSION_KEY = 'permission_session_key'
# 菜单字典数据
MENU_SESSION_KEY = 'menu_session_key'
# 白名单
VALID_URL_LIST = [
    '/login/',
    '/wxlogin/',
    '/admin/.*',
    '/xadmin/.*',
    '/api/.*',
    '/docs/.*',
    '/ueditor/.*',
    '/elfinder/.*',
]

# 需要登录但无需权限的URL
NO_PERMISSION_LIST = [
    '/index/',
    '/logout/',
    '/media/.*',
    '/docs/.*',
    '/ueditor/.*',
    '/elfinder/.*',
]
# 自动化发现路由中URL时，排除的URL
AUTO_DISCOVER_EXCLUDE = [
    '/admin/.*',
    '/login/',
    '/logout/',
    '/index/',
    '/xadmin/.*',
    '/media/.*',
    '/api/.*',
    '/api-auth/.*',
    '/docs/.*',
    '/ueditor/.*',
    '/elfinder/.*',
    '/wxlogin/',
    '/work/',
]

#DRF相关配置
REST_FRAMEWORK = {

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser'
    )
}
#JWT相关设置
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

#LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}  # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            },
        # 下面是django自带的最详细的输出
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/all.log'),     # 日志输出文件，根目录下需要手动新建
            'maxBytes': 1024*1024*5,                  # 文件大小5M
            'backupCount': 5,                         # 备份份数
            'formatter': 'standard',                   # 使用哪种formatters日志格式上面定义了standard
        },
        # 下面是django自带的控制台输出
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 下面是django自带的5xx或者4xx错误记录在script.log里
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            },
        # 下面是django自带的脚本错误记录
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,'logs/script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            }
    },
    # 下面是定义日志器
    'loggers': {

        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django_auth_ldap': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,  # 是否继承父类
            },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        # 下面是给views调用使用的
        'asset': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'wiki': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'webterminal': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'ansible_task': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

# Channels settings
CHANNEL_LAYERS = {
    "default": {
       "BACKEND": "asgi_redis.RedisChannelLayer",  # use redis backend
       "CONFIG": {
           "hosts": [("localhost", 6379)],  # set redis address
           "channel_capacity": {
                                   "http.request": 1000,
                                   "websocket.send*": 10000,
                                },
           "capacity": 10000,
           },
       "ROUTING": "opadmin.routing.channel_routing",  # load routing from our routing.py file
       },
}

# List of upload handler classes to be applied in order.
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
# 允许内存中上传文件的大小
#   合法：InMemoryUploadedFile对象（写在内存）         -> 上传文件小于等于 FILE_UPLOAD_MAX_MEMORY_SIZE
# 不合法：TemporaryUploadedFile对象（写在临时文件）     -> 上传文件大于    FILE_UPLOAD_MAX_MEMORY_SIZE 且 小于 DATA_UPLOAD_MAX_MEMORY_SIZE
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
# 允许上传内容的大小（包含文件和其他请求内容）
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum number of GET/POST parameters that will be read before a
# SuspiciousOperation (TooManyFieldsSent) is raised.
# 允许的上传文件数
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

# Directory in which upload streamed files will be temporarily saved. A value of
# `None` will make Django use the operating system's default temporary directory
# (i.e. "/tmp" on *nix systems).
# 临时文件夹路径
FILE_UPLOAD_TEMP_DIR = None

# The numeric mode to set newly-uploaded files to. The value should be a mode
# you'd pass directly to os.chmod; see https://docs.python.org/3/library/os.html#files-and-directories.
# 文件权限
FILE_UPLOAD_PERMISSIONS = None

# The numeric mode to assign to newly-created directories, when uploading files.
# The value should be a mode as you'd pass to os.chmod;
# see https://docs.python.org/3/library/os.html#files-and-directories.
# 文件夹权限
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

#celery相关配置参数
#CELERY_BROKER_URL = 'redis://localhost:6379/6'
#CELERY_BROKER_URL = 'amqp://opadmin:opadmin@127.0.0.1:5672/myhost'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERYD_MAX_TASKS_PER_CHILD = 40
CELERY_TRACK_STARTED = True
#CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# 这是使用了django-celery默认的数据库调度模型,任务执行周期都被存在你指定的orm数据库中
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERY_ROUTES = {
    'assets.tasks.*': {'queue': 'default', 'routing_key': 'default'},
    'ansible_task.tasks.*': {'queue': 'ansible', 'routing_key': 'ansible'},
}

# 执行ansible命令使用的redis信息
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 2
REDIS_PASSWORD = None

ANSIBLE_ROLE_PATH = os.path.join(MEDIA_ROOT, 'roles')

TIME_FORMAT = '%Y-%m-%d %X'


# session 设置
# 30分钟
SESSION_COOKIE_AGE = 60 * 30
SESSION_SAVE_EVERY_REQUEST = True
# 关闭浏览器，则COOKIE失效
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ** 系统发件箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
# 所用邮箱的smtp地址
EMAIL_HOST = ''
EMAIL_PORT = 25
# 邮箱地址
EMAIL_HOST_USER = ''
# 邮箱密码
EMAIL_HOST_PASSWORD = ''
# 发件箱名字，和邮箱地址一样就行了
DEFAULT_FROM_EMAIL = ''

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}