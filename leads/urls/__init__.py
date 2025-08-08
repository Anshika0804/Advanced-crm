from leads.urls.lead_url import urlpatterns as lead_urlpatterns
from leads.urls.ticket_urls import urlpatterns as ticket_urlpatterns
# from leads.urls.note_urls import urlpatterns as note_urlpatterns
# from leads.urls.attachment_urls import urlpatterns as attachment_urlpatterns
# from leads.urls.campaign_urls import urlpatterns as campaign_urlpatterns

urlpatterns = (
    lead_urlpatterns +
    ticket_urlpatterns
    # note_urlpatterns +
    # attachment_urlpatterns +
    # campaign_urlpatterns
)
