import typing as t
import warnings

from .gui import Gui
from .state import State
from .partial import Partial


def download(state: State, content: t.Any, name: t.Optional[str] = "", on_action: t.Optional[str] = ""):
    """Donwload content to the client.

    Arguments:
        state: the current user state as received in any callback.
        content: file path or file content
        name: file name for the content on the client browser (default to content name)
        on_action: function called when the download starts
    """
    if state and isinstance(state._gui, Gui):
        state._gui._download(content, name, on_action)
    else:
        warnings.warn("'download()' must be called in the context of a callback")


def notify(
    state: State,
    notification_type: str = "I",
    message: str = "",
    browser_notification: t.Optional[bool] = None,
    duration: t.Optional[int] = None,
):
    """Send a notification to the user interface.

    Arguments:
        state: the current user state as received in any callback.
        notification_type: the notification type. This can be one of `"success"`, `"info"`, `"warning"`, or `"error"`.
            To remove the last notification, set this parameter to the empty string.
        message: the text message to display.
        browser_notification: if True, the browser will also show the notification.
            If not specified or set to None, this parameter will use the value of
            `configuration[browser_notification]`.
        duration: the time, in milliseconds, during which the notification is shown.
            If not specified or set to None, this parameter will use the value of
            `configuration[notification_duration]`.

    Note that you can also call this function with _notification_type_ set to the first letter
    or the alert type (ie setting _notification_type_ to "i" is equivalent to setting it to
    "info").
    """
    if state and isinstance(state._gui, Gui):
        state._gui._notify(notification_type, message, browser_notification, duration)
    else:
        warnings.warn("'notify' function should be called in the context of a callback")


def hold_control(
    state: State,
    callback: t.Optional[t.Union[str, t.Callable]] = None,
    message: t.Optional[str] = "Work in Progress...",
):
    """Hold the User Interface actions.

    When the User Interface is held, users cannot interact with visual elements.<br/>
    The application must call `resume_control()^` so that users can interact again
    with the visual elements.

    Arguments:
        state: the current user state as received in any callback.
        callback: the function to be called on _callback_. If empty or None, no cancel action
            is provided to the user.
        message: the message to show.
    """
    if state and isinstance(state._gui, Gui):
        state._gui._hold_actions(callback, message)
    else:
        warnings.warn("'hold_actions()' must be called in the context of a callback")


def resume_control(state: State):
    """Resume the User Interface actions.

    This function must be called after `hold_control()^` was invoked, when interaction
    must be allowed again for the user.

    Arguments:
        state: the current user state as received in any callback.
    """
    if state and isinstance(state._gui, Gui):
        state._gui._resume_actions()
    else:
        warnings.warn("'resume_actions()' must be called in the context of a callback")


def navigate(state: State, to: t.Optional[str] = ""):
    """Navigate to a page.

    Arguments:
        state: the current user state as received in any callback.
        to: the name of the page to navigate to. This must be a valid page identifier.
            If ommitted, the application navigates to the root page.
    """
    if state and isinstance(state._gui, Gui):
        state._gui._navigate(to)
    else:
        warnings.warn("'navigate()' must be called in the context of a callback")

def refresh_partial(state: State, partial: Partial, content: str):
    if state and isinstance(state._gui, Gui):
        state._gui._refresh_partial(partial, content)
    else:
        warnings.warn("'refresh_partial()' must be called in the context of a callback")
