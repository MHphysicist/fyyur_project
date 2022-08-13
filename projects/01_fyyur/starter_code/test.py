from app import db, Venue, Show

data = []
vlist = db.session.query(Venue).order_by(Venue.city, Venue.state)
leng = vlist.count()

vl = []
count = 0
while count < leng - 1:
  v = vlist[count]
  item = {"city": v.city, "state": v.state}
  if item not in vl:
    vl.append(item.copy())
    item.update({"venues": [{
      "id" : v.id,
      "name" : v.name,
      "num_upcoming_shows" : Venue.query.join(Show).filter(Venue.name==v.name,Venue.id==Show.venue_id).count()}]}
      )
    data.append(item)
    print("count + 1 = " + str(count))
  else:
    print("count - 1 = " + str(count))
    data[len(data)-1]["venues"].append({
      "id" : v.id,
      "name" : v.name,
      "num_upcoming_shows" : Venue.query.join(Show).filter(Venue.name==v.name,Venue.id==Show.venue_id).count()}
      )
  count = count + 1


for d in data:
  print(d['city'], d['state'])
  for fe in d['venues']:
    print(fe['id'], fe['name'], fe['num_upcoming_shows'])
    print('\n')