import logging
from settings.models import WebSettings

logger = logging.getLogger(__name__)


def webSettingsUnivarsal(request):
    context = {
        'webSettingsUniversal': '',
    }
    try:
        webSettingsUniversal = WebSettings.objects.first()

        if not webSettingsUniversal:
            raise ValueError("No settings available in the WebsiteSettings table.")

        context.update({
            'webSettingsUniversal': webSettingsUniversal,
        })

    except WebSettings.DoesNotExist:
        # This block should log the absence of any settings and possibly use default settings
        logger.warning("WebsiteSettings does not exist. Using default settings.")
        return {'webSettingsUniversal': ''}

    except AttributeError as e:
        # Handle any attribute error and log it
        logger.error(f"An attribute error occurred: {e}. Using default settings for the missing attributes.")
        return {'webSettingsUniversal': ''}

    except ValueError as e:
        # Handle the custom exception raised above
        logger.error(f"ValueError: {e}. Using default settings.")
        return {'webSettingsUniversal': ''}

    except Exception as e:
        # This is a general exception handler. Use this sparingly and only for unexpected errors.
        logger.critical(f"Unexpected error occurred when fetching site settings: {e}. Using default settings.")
        return {'webSettingsUniversal': ''}

    return context