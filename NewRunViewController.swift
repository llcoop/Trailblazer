extension NewRunViewController: CLLocationManagerDelegate {

  func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
    for newLocation in locations {
      let howRecent = newLocation.timestamp.timeIntervalSinceNow
      guard newLocation.horizontalAccuracy < 20 && abs(howRecent) < 10 else { continue }

      if let lastLocation = locationList.last {
        let delta = newLocation.distance(from: lastLocation)
        distance = distance + Measurement(value: delta, unit: UnitLength.meters)
      }

      locationList.append(newLocation)
    }
  }
  private func mapRegion() -> MKCoordinateRegion? {
  guard
    let locations = run.locations,
    locations.count > 0
  else {
    return nil
  }
    
  let latitudes = locations.map { location -> Double in
    let location = location as! Location
    return location.latitude
  }
    
  let longitudes = locations.map { location -> Double in
    let location = location as! Location
    return location.longitude
  }
    
  let maxLat = latitudes.max()!
  let minLat = latitudes.min()!
  let maxLong = longitudes.max()!
  let minLong = longitudes.min()!
    
  let center = CLLocationCoordinate2D(latitude: (minLat + maxLat) / 2,
                                      longitude: (minLong + maxLong) / 2)
  let span = MKCoordinateSpan(latitudeDelta: (maxLat - minLat) * 1.3,
                              longitudeDelta: (maxLong - minLong) * 1.3)
  return MKCoordinateRegion(center: center, span: span)
}

private func configureView() {
  let distance = Measurement(value: run.distance, unit: UnitLength.meters)
  let seconds = Int(run.duration)
  let formattedDistance = FormatDisplay.distance(distance)
  let formattedDate = FormatDisplay.date(run.timestamp)
  let formattedTime = FormatDisplay.time(seconds)
  let formattedPace = FormatDisplay.pace(distance: distance, 
                                         seconds: seconds, 
                                         outputUnit: UnitSpeed.minutesPerMile)
  
  distanceLabel.text = "Distance:  \(formattedDistance)"
  dateLabel.text = formattedDate
  timeLabel.text = "Time:  \(formattedTime)"
  paceLabel.text = "Pace:  \(formattedPace)"
}
  private func saveRun() {
  let newRun = Run(context: CoreDataStack.context)
  newRun.distance = distance.value
  newRun.duration = Int16(seconds)
  newRun.timestamp = Date()
  
  for location in locationList {
    let locationObject = Location(context: CoreDataStack.context)
    locationObject.timestamp = location.timestamp
    locationObject.latitude = location.coordinate.latitude
    locationObject.longitude = location.coordinate.longitude
    newRun.addToLocations(locationObject)
  }
  
  CoreDataStack.saveContext()
  
  run = newRun
}
}