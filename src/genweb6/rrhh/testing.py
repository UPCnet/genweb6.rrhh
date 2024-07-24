# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE

from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import genweb6.rrhh


class Genweb6RRHHLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=genweb6.rrhh)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'genweb6.rrhh:default')


GENWEB6_RRHH_FIXTURE = Genweb6RRHHLayer()


GENWEB6_RRHH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEB6_RRHH_FIXTURE,),
    name='Genweb6RRHHLayer:IntegrationTesting',
)


GENWEB6_RRHH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEB6_RRHH_FIXTURE,),
    name='Genweb6RRHHLayer:FunctionalTesting',
)


GENWEB6_RRHH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GENWEB6_RRHH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Genweb6RRHHLayer:AcceptanceTesting',
)
