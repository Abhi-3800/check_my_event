from django.urls import path
from . import views

urlpatterns = [
	#int, path(whole urls), slug(- and _), UUID(universally unique identifier), str are path converters
	path('', views.home, name="home"),
	path('<int:year>/<str:month>/', views.home, name='home'),
	path('events', views.all_events, name='list-events'),
	path('add_venue', views.add_venue, name='add-venue'),
	path('list_venues', views.list_venues, name='list-venues'),
	path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
	path('search_venues', views.search_venues, name='search-venues'),
	path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
	path('add_event', views.add_event, name='add-event'),
	path('update_event/<event_id>', views.update_event, name='update-event'),
	path('delete_event/<event_id>', views.delete_event, name="delete-event"),
	path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
	path('venue_text', views.venue_text, name='venue_text'),
	]