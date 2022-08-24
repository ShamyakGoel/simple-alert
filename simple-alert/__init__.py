from termcolor import cprint
import sys
default_success_color = 'green'
default_error_color = 'red'
default_info_color = 'blue'
def config(**kwargs):
    """
    Config function to change default colors.
    """
    global default_success_color, default_error_color, default_info_color
    if kwargs.get('success_color') is not None:
        default_success_color = kwargs.get('success_color')
    if kwargs.get('info_color') is not None:
        default_info_color = kwargs.get('info_color')
    if kwargs.get('error_color') is not None:
        default_error_color = kwargs.get('error_color')
def custom_alert(type_alert:str, color: str, alert:str, highlight=False, attrs=[]):
    """
    Gives a custom alert. Same parameters of alert except color.
    """
    if sys.version_info >= (3,10):
        match highlight:
            case True:
                cprint(f'{type_alert}! ' + alert, color=color, attrs=attrs)
            case False:
                cprint(f'{type_alert}! ' + alert, on_color='on_'+color, attrs=attrs)
    else:
        if not highlight:
            cprint(f'{type_alert}! ' + alert, on_color='on_'+color, attrs=attrs)
        elif highlight:
            cprint(f'{type_alert}! ' + alert, color=color, attrs=attrs)
def alert(alert_type : str='success', alert:str='', highlight=False, attrs=[]):
    """
    A function to give alert\n
    alert_type can be success, error, warning or info.\n
    alert is the text that you want to give as an alert.\n
    highlight defines whether text should be highlighted or not.\n
    attrs can have bold, dark, underline, blink, reverse, concealed.
    """
    if sys.version_info >= (3,10):
        match alert_type:
            case 'success' if not highlight:
                cprint('Success! ' + alert, color=default_success_color, attrs=attrs)
            case 'success' if highlight:
                cprint('Success! ' + alert, on_color='on_'+default_success_color, attrs=attrs)
            case 'error' if not highlight:
                cprint('Error! ' + alert, color=default_error_color, attrs=attrs)
            case 'error' if highlight:
                cprint('Error! ' + alert, on_color='on_'+default_error_color, attrs=attrs)
            case 'info' if not highlight:
                cprint('Info! ' + alert, color=default_info_color, attrs=attrs)
            case 'info' if highlight:
                cprint('Info! ' + alert, on_color='on_'+default_info_color, attrs=attrs)
    else:
        if alert_type == 'success' and not highlight:
            cprint('Success! ' + alert, color='green', attrs=attrs)
        elif alert_type == 'success' and highlight:
            cprint('Success! ' + alert, on_color='on_green', attrs=attrs)
        elif alert_type == 'error' and not highlight:
            cprint('Error! ' + alert, color='red', attrs=attrs)
        elif alert_type == 'error' and highlight:
            cprint('Error! ' + alert, on_color='on_red', attrs=attrs)
        elif alert_type == 'info' and not highlight:
            cprint('Info! ' + alert, color='blue', attrs=attrs)
        elif alert_type == 'info' and highlight:
            cprint('Info! ' + alert, on_color='on_blue', attrs=attrs)
