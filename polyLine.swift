private func polyLine() -> [MulticolorPolyline] {
    
  // 1
  let locations = run.locations?.array as! [Location]
  var coordinates: [(CLLocation, CLLocation)] = []
  var speeds: [Double] = []
  var minSpeed = Double.greatestFiniteMagnitude
  var maxSpeed = 0.0
    
  // 2
  for (first, second) in zip(locations, locations.dropFirst()) {
    let start = CLLocation(latitude: first.latitude, longitude: first.longitude)
    let end = CLLocation(latitude: second.latitude, longitude: second.longitude)
    coordinates.append((start, end))
      
    //3
    let distance = end.distance(from: start)
    let time = second.timestamp!.timeIntervalSince(first.timestamp! as Date)
    let speed = time > 0 ? distance / time : 0
    speeds.append(speed)
    minSpeed = min(minSpeed, speed)
    maxSpeed = max(maxSpeed, speed)
  }
    
  //4
  let midSpeed = speeds.reduce(0, +) / Double(speeds.count)
    
  //5
  var segments: [MulticolorPolyline] = []
  for ((start, end), speed) in zip(coordinates, speeds) {
    let coords = [start.coordinate, end.coordinate]
    let segment = MulticolorPolyline(coordinates: coords, count: 2)
    segment.color = segmentColor(speed: speed,
                                 midSpeed: midSpeed,
                                 slowestSpeed: minSpeed,
                                 fastestSpeed: maxSpeed)
    segments.append(segment)
  }
  return segments
}