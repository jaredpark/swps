from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class AccountApphook(CMSApp):
    name = _("Account Apphook")
    urls = ["accounts.urls"]

apphook_pool.register(AccountApphook)