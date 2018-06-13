# Local passwords and stuff not to be shared with GIT

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u7!-y4k1c6b44q507nr_l+c^12o7ur++cpzyn!$65w^!gum@h%'

# DATABASE INFORMATION

GCLOUD_HOST = '/cloudsql/your-gcloud-connectionName'
GCLOUD_NAME = 'your-gcloud-databse-name'
GCLOUD_USER = 'your-gcloud-username'
GCLOUD_PASSWORD = 'your-gcloud-password'

# the address your emails (save the dates/invites/etc.) will come from
DEFAULT_WEDDING_FROM_EMAIL = 'You and Your Partner <happilyeverafter@example.com>'
# the default reply-to of your emails
DEFAULT_WEDDING_REPLY_EMAIL = 'happilyeverafter@example.com'
