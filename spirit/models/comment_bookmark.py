# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

from ..utils import paginator


@python_2_unicode_compatible
class CommentBookmark(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"))
    topic = models.ForeignKey('spirit.Topic')

    comment_number = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'topic')
        verbose_name = _("comment bookmark")
        verbose_name_plural = _("comments bookmarks")

    def get_absolute_url(self):
        return paginator.get_url(self.topic.get_absolute_url(),
                                 self.comment_number,
                                 settings.ST_COMMENTS_PER_PAGE,
                                 settings.ST_COMMENTS_PAGE_VAR)

    def __str__(self):
        return "%s bookmarked comment %s in %s" % (self.user.username,
                                                   self.topic.title,
                                                   self.comment_number)
