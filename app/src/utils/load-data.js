import * as d3 from 'd3';
import axios from 'axios';

export async function loadData(datafile, isUrl = false) {
  let data;
  if (isUrl) {
    const fileType = datafile.split('f=').pop();
    if (fileType === 'csv') {
      data = await d3.csv(datafile, d3.autoType);
    } else if (fileType === 'psv') {
      data = await d3.dsv('|', datafile, d3.autoType);
    } else if (fileType === 'geojson' || fileType === 'json') {
      const response = await axios.get(datafile);
      data = response.data;
    } else {
      console.log("Error")
      throw new Error(`Unsupported file type: ${fileType}`);
    }
  } else {
    const fileType = datafile.split('.').pop();
    if (fileType === 'csv') {
      data = await d3.csv(datafile, d3.autoType);
    } else if (fileType === 'psv') {
      data = await d3.dsv('|', datafile, d3.autoType);
    } else if (fileType === 'geojson') {
      const response = await axios.get(datafile);
      data = response.data;
    } else {
      throw new Error(`Unsupported file type: ${fileType}`);
    }
  }
  return data;
}
