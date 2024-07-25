# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView

from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.dexterity.interfaces import IDexteritySchema
from plone.supermodel import model
from zope.interface import implementer

from genweb6.core import _


class IDocumentRRHH(model.Schema, IDexteritySchema):

    contingut = RichText(
        title=_(u"Contingut"),
        required=False,
    )


@implementer(IDocumentRRHH)
class DocumentRRHH(Container):
  pass


class View(BrowserView):
    pass
