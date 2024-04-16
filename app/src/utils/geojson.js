import * as Wkt from 'wicket';
// utility functions to convert to / from geojson
export async function flatten_geojson(features){
  if( features.length ){
    var returnValue = features.map( (feature) => {
        var _wkt = new Wkt.Wkt();
        var result = feature.properties;
        _wkt.read(JSON.stringify(feature.geometry));
        result.location = "SRID=4326; " + _wkt.write();
        result.id = feature.id;
        return result;
    })
    return returnValue;
  }
};

export function to_geojson(rows){

  const nullify_empty_strings = (key, value) => {
    return value === '' ? null: value;
  }

  if( rows.length ){
    console.log(rows)
    var returnValue = rows.map( (row) => {
      console.log(row);
      const coords = row.location.match(/POINT\(([-\d\.]+)\s+([-\d\.]+)\)/);
      const latlng = [parseFloat(coords[1]), parseFloat(coords[2])];
      var geojson = {
        id: row.id,
        type: 'Feature',
        properties: JSON.parse(JSON.stringify(row, nullify_empty_strings)),
        geometry: {
          type: 'Point',
          coordinates: latlng
        }
      };
      // remove id and location
      delete geojson.properties.id;
      delete geojson.properties.location;
      return geojson;
    })
    console.log(rows)
    return returnValue;
  }
};
