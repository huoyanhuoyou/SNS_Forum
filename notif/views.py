import logging

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Notification
from django.db.models import Q
from django.conf import settings


logger = logging.getLogger(__name__)
User = get_user_model()

@login_required
def notification_list(request):
    logger.debug("notification_list called by user %s" % request.user)
    #notifications_qs = Notification.objects.filter(user=request.user).order_by("-timestamp")
    notifications_qs = Notification.objects.filter(Q(sender=request.user) | Q(user=request.user)).order_by("-timestamp")
    new_notifs = notifications_qs.filter(viewed=False)
    old_notifs = notifications_qs.filter(viewed=True)
    logger.debug(
        "User %s has %s unread and %s read notifications",
        request.user,
        len(new_notifs),
        len(old_notifs)
    )
    context = {
        'read': old_notifs,
        'unread': new_notifs,
    }
    return render(request, 'list.html', context)
    new_notifs = notifications_qs.filter(viewed=False)
    old_notifs = notifications_qs.filter(viewed=True)
    logger.debug(
        "User %s has %s unread and %s read notifications",
        request.user,
        len(new_notifs),
        len(old_notifs)
    )
    context = {
        'read': old_notifs,
        'unread': new_notifs,
    }
    return render(request, 'list.html', context)


@login_required
def notification_view(request, notif_id):
    logger.debug(
        "notification_view called by user %s for notif_id %s",
        request.user,
        notif_id
    )
    notif = get_object_or_404(Notification, pk=notif_id)
    if notif.user == request.user:
        logger.debug("Providing notification for user %s", request.user)
        context = {'notif': notif}
        notif.mark_viewed()
        return render(request, 'view.html', context)
    else:
        logger.warning(
            "User %s not authorized to view notif_id %s belonging to user %s",
            request.user,
            notif_id, notif.user
        )
        messages.error(request, _('You are not authorized to view that notification.'))
        return redirect('notif:notiflist')


@login_required
def remove_notification(request, notif_id):
    logger.debug(
        "remove notification called by user %s for notif_id %s",
        request.user,
        notif_id
    )
    notif = get_object_or_404(Notification, pk=notif_id)
    if notif.user == request.user:
        if Notification.objects.filter(id=notif_id).exists():
            notif.delete()
            logger.info("Deleting notif id %s by user %s", notif_id, request.user)
            messages.success(request, _('Deleted notification.'))
    else:
        logger.error(
            "Unable to delete notif id %s for user %s - notif matching id not found.",
            notif_id,
            request.user
        )
        messages.error(request, _('Failed to locate notification.'))
    return redirect('notif:notiflist')


@login_required
def mark_all_read(request):
    logger.debug('mark all notifications read called by user %s', request.user)
    Notification.objects.filter(user=request.user).update(viewed=True)
    messages.success(request, _('Marked all notifications as read.'))
    return redirect('notif:notiflist')


@login_required
def delete_all_read(request):
    logger.debug('delete all read notifications called by user %s', request.user)
    Notification.objects.filter(user=request.user).filter(viewed=True).delete()
    messages.success(request, _('Deleted all read notifications.'))
    return redirect('notif:notiflist')


def user_notifications_count(request, user_pk: int):
    """returns to notifications count for the give user as JSON

    This view is public and does not require login
    """
    unread_count = Notification.objects.user_unread_count(user_pk)
    data = {'unread_count': unread_count}
    return JsonResponse(data, safe=False)

@login_required
def leave_message(request, receiver_username):
    if request.method == 'POST':
        user = User.objects.get(username=receiver_username)
        content = request.POST.get('content')
        imessage = Notification(sender=request.user, user=user, mes=content)
        imessage.save()
        messages.success(request, 'Message sent successfully.')
        return redirect('notif:notiflist')
    else:
        return render(request, 'send_message.html')  # Create a template for sending messages