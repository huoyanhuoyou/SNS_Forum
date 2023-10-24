import logging

from django.db import models
from django.conf import settings

logger = logging.getLogger(__name__)
class Notification(models.Model):
    """Notification to a user within Auth"""

    NOTIFICATIONS_MAX_PER_USER_DEFAULT = 100#最大通知数量
    NOTIFICATIONS_REFRESH_TIME_DEFAULT = 30#通知刷新时间

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    mes = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    viewed = models.BooleanField(default=False, db_index=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    #receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']


    def __str__(self) -> str:#notification类的描写
        return f"{self.user}: {self.title}"

    def save(self, *args, **kwargs):
        # overriden save to ensure cache is invaidated on very call
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        # overriden delete to ensure cache is invaidated on very call
        super().delete(*args, **kwargs)


    def mark_viewed(self) -> None:# 将通知标记为已查看，并保存该更改。
        """Mark notification as viewed."""
        logger.info("Marking notification as viewed: %s" % self)
        self.viewed = True
        self.save()
