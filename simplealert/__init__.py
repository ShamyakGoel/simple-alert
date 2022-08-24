from termcolor import cprint
import sys
__all__ = ['config', 'custom_alert', 'alert']
_cprint = cprint

del cprint
default_success_color = 'green'
default_error_color = 'red'
default_info_color = 'blue'
default_warning_color = 'yellow'
"""
Module that gives alert on terminal.
FUNCTIONS:
    config: See config documentation
    custom_alert: See custom_alert documentation
    alert: See alert documentation
"""
def config(**kwargs):
    """
    Config function to change default colors.\n
    Params:\n
    success_color=color you want in success alert\n
    error_color=color you want in error alert\n
    info_color=color you want in info alert\n
    warning_color=color you want in warning alert\n
    """
    global default_success_color, default_error_color, default_info_color,default_warning_color
    if kwargs.get('success_color') is not None:
        default_success_color = kwargs.get('success_color')
    if kwargs.get('info_color') is not None:
        default_info_color = kwargs.get('info_color')
    if kwargs.get('error_color') is not None:
        default_error_color = kwargs.get('error_color')
    if kwargs.get('warning_color') is not None:
        default_warning_color = kwargs.get('warning_color')
def custom_alert(type_alert:str, color: str, alert:str, highlight=False, attrs=[]):
    """
    Gives a custom alert. Same parameters of function alert except color.
    """
    if sys.version_info >= (3,10):
        match highlight:
            case False:
                _cprint(f'{type_alert}! ' + alert, color=color, attrs=attrs)
            case True:
                _cprint(f'{type_alert}! ' + alert, on_color='on_'+color, attrs=attrs)
    else:
        if highlight:
            _cprint(f'{type_alert}! ' + alert, on_color='on_'+color, attrs=attrs)
        elif not highlight:
            _cprint(f'{type_alert}! ' + alert, color=color, attrs=attrs)
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
                _cprint('Success! ' + alert, color=default_success_color, attrs=attrs)
            case 'success' if highlight:
                _cprint('Success! ' + alert, on_color='on_'+default_success_color, attrs=attrs)
            case 'error' if not highlight:
                _cprint('Error! ' + alert, color=default_error_color, attrs=attrs)
            case 'error' if highlight:
                _cprint('Error! ' + alert, on_color='on_'+default_error_color, attrs=attrs)
            case 'info' if not highlight:
                _cprint('Info! ' + alert, color=default_info_color, attrs=attrs)
            case 'info' if highlight:
                _cprint('Info! ' + alert, on_color='on_'+default_info_color, attrs=attrs)
            case 'warning' if not highlight:
                _cprint('Warning! ' + alert, color=default_warning_color, attrs=attrs)
            case 'warning' if highlight:
                _cprint('Warning! ' + alert, on_color='on_'+default_warning_color, attrs=attrs)
    else:
        if alert_type == 'success' and not highlight:
            _cprint('Success! ' + alert, color=default_success_color, attrs=attrs)
        elif alert_type == 'success' and highlight:
            _cprint('Success! ' + alert, on_color='on_'+default_success_color, attrs=attrs)
        elif alert_type == 'error' and not highlight:
            _cprint('Error! ' + alert, color=default_error_color, attrs=attrs)
        elif alert_type == 'error' and highlight:
            _cprint('Error! ' + alert, on_color='on_'+default_error_color, attrs=attrs)
        elif alert_type == 'info' and not highlight:
            _cprint('Info! ' + alert, color=default_info_color, attrs=attrs)
        elif alert_type == 'info' and highlight:
            _cprint('Info! ' + alert, on_color='on_'+default_info_color, attrs=attrs)
        elif alert_type == 'warning' and not highlight:
            _cprint('Warning! ' + alert, color=default_warning_color, attrs=attrs)
        elif alert_type == 'warning' and highlight:
            _cprint('Warning! ' + alert, on_color='on_'+default_warning_color, attrs=attrs)