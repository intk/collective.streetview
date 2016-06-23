from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.dexterity.browser.view import DefaultView
from zope.interface import implementer

from collective.streetview import MessageFactory as _

class IStreetView(form.Schema):
    """
    Information about Google StreetView
    """


@implementer(IStreetView)
class StreetView(Container):
    """Convenience subclass for ``StreetView`` portal type
    """
    streetview_settings = schema.Text(
        title=_(u'streetview_settings', default="StreetView settings"),
        description=_(u'streetview_description', default="Add StreetView settings as a JSON string.")
        required=False
    )


class StreetViewView(DefaultView):
    pass

