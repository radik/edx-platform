def plugin_settings(settings):
    settings.ACE_ENABLED_CHANNELS = [
        'django_email'
    ]
    settings.ACE_ENABLED_POLICIES = [
        'bulk_email_optout'
    ]
    settings.ACE_CHANNEL_SAILTHRU_DEBUG = True
    settings.ACE_CHANNEL_SAILTHRU_TEMPLATE_NAME = 'Automated Communication Engine Email'
    settings.ACE_CHANNEL_SAILTHRU_API_KEY = None
    settings.ACE_CHANNEL_SAILTHRU_API_SECRET = None

    email_getter = 'openedx.core.djangoapps.site_configuration.helpers:get_email_from_address'
    settings.ACE_CHANNEL_DJANGO_FROM_ADDRESS_GETTER = email_getter

    settings.ACE_ROUTING_KEY = 'edx.core.low'

    settings.FEATURES['test_django_plugin'] = True
