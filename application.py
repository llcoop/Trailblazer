""" Trailblazer v0.1	
	Mobile application for ECE/CREG 258 Project
	Authors: Logan Cooper and Shreshth Awadhiya
	Project Advisor: Mark Erle
"""
import ui
import typing
import console
import notification
import Map
import location
import time

###	Constants
# Names of the .pyui files
SPLASH_SCREEN = "splash_screen"
ROUTE_SELECT = "route_select"
ROUTE_DISPLAY = "route_display"
ROUTE_RECORD = "route_record"

MAP_ZOOM = 0.001
MAP_FRAME = [81, 108, 252, 252]
MAP_UPDATE_TIME = 3

###	Global Vars
active = SPLASH_SCREEN

###	Methods
def __init__():
	view = ui.load_view(active)
	map = Map.MapView(frame=(81, 108, 252, 252))
	view.add_subview(map)
	view.present(orientations = ['portait'])
	
	location.start_updates()
	time.sleep(MAP_UPDATE_TIME)
	loc = location.get_location()
	location.stop_updates()

	# Update the map in the splash screen
	if loc:
		lat, lon = loc['latitude'], loc['longitude']
		map.set_region(lat, lon, MAP_ZOOM, MAP_ZOOM, animated=True)
		map.add_pin(lat, lon, 'Current Location', str((lat, lon)))

	"""
	while (active == SPLASH_SCREEN):
		location.start_updates()
		time.sleep(MAP_UPDATE_TIME)
		loc = location.get_location()
		location.stop_updates()
		lat, lon = loc['latitude'], loc['longitude']
		map.set_region(lat, lon, MAP_ZOOM, MAP_ZOOM, animated=True)
		map.add_pin(lat, lon, 'Current Location', str((lat, lon)))
	"""	
	location.stop_updates()
	pass
	
## UI transitions
# UI transition to Routes Page
def switchToRoutes(sender):
	active = ROUTE_SELECT
	view = ui.load_view(active)
	view.present(orientations = ['portrait'])
	pass

# UI transition to Splash Page
def switchToSplash(sender):
	active = SPLASH_SCREEN
	view = ui.load_view(active)
	map = Map.MapView(frame=(81, 108, 252, 252))
	view.add_subview(map)
	view.present(orientations = ['portrait'])

	location.start_updates()
	time.sleep(MAP_UPDATE_TIME)
	loc = location.get_location()
	location.stop_updates()

	# Update the map in the splash screen
	if loc:
		lat, lon = loc['latitude'], loc['longitude']
		map.set_region(lat, lon, MAP_ZOOM, MAP_ZOOM, animated=True)
		map.add_pin(lat, lon, 'Current Location', str((lat, lon)))


	pass

# UI transiiton to Route Display Page
def switchToRouteDisplay(sender):
	global active
	active = ROUTE_DISPLAY
	view = ui.load_view(active)
	map = Map.MapView(frame=(81, 108, 252, 252))
	view.add_subview(map)
	view.present(orientations = ['portrait'])

	location.start_updates()
	time.sleep(MAP_UPDATE_TIME)
	loc = location.get_location()
	location.stop_updates()

	# Update the map in the Route Display
	if loc:
		lat, lon = loc['latitude'], loc['longitude']
		map.set_region(lat, lon, MAP_ZOOM, MAP_ZOOM, animated=True)
		map.add_pin(lat, lon, 'Current Location', str((lat, lon)))
	
	"""
	while (active == ROUTE_DISPLAY):
		location.start_updates()
		time.sleep(MAP_UPDATE_TIME)
		loc = location.get_location()
		location.stop_updates()
		lat, lon = loc['latitude'], loc['longitude']
		map.set_region(lat, lon, MAP_ZOOM, MAP_ZOOM, animated=True)
		map.add_pin(lat, lon, 'Current Location', str((lat, lon)))
	"""
	pass

# UI transition to Route Record Page
def switchToRouteRecord(sender):
	active = ROUTE_RECORD
	view = ui.load_view(active)
	map = Map.MapView(frame=(81, 108, 252, 252))
	view.add_subview(map)
	view.present(orientations = ['portrait'])

	location.start_updates()
	time.sleep(MAP_UPDATE_TIME)
	loc = location.get_location()
	location.stop_updates()

	if loc:
		lat, lon = loc['latitude'], loc['longitude']
		map.set_region(lat, lon, MAP_ZOOM, MAP_ZOOM, animated=True)
		map.add_pin(lat, lon, 'Current Location', str((lat, lon)))

	pass

## App logic
# Button binding to start recording a route
def startRouteRecord(sender):
	switchToRouteRecord(sender)
	#TODO: Implement Function
	pass

# Button binding to end recording a route
def endRouteRecord(sender):
	result = console.input_alert('Save Route?', 'Enter a name for your route:')
	switchToSplash(sender)
	#TODO: Implement Function
	pass

# Button binding to play a selected route
def playRoute(sender):
	switchToRouteDisplay(sender)
	#TODO: Implement Function
	pass

# Button binding to stop a selected route
def stopRoute(sender):
	switchToSplash(sender)
	#TODO: Implement Function
	pass

# Button binding to pause a selected route
def pauseRoute(sender):
	#TODO: Implement Function
	pass

# Button binding to resume a selected route
def resumeRoute(sender):
	#TODO: Implement Function
	pass

# Button binding to select a route
def routeStats(sender):
	alert = notification.schedule(message = 'Route Stats: ')
	#TODO: Implement Function
	pass

# Button binding to select a route
def selectRoute(sender):
	alert = notification.schedule(message = 'Route Selected')
	#TODO: Implement Function
	pass

# Button binding to delete a selected route
def deleteRoute(sender):
	alert = notification.schedule(message = 'Route Deleted')
	#TODO: Implement Function
	pass

# Button binding to edit a selected route
def accAction(sender):
	alert = notification.schedule(message = 'Acc Action')
	#TODO: Implement Function
	pass

def main():
	__init__()

main()
