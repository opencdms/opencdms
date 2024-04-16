// Script loads list of components to include in navigation draw from registry.json
//
'use strict'

// import registry from './registry.json'
var registry = require("./registry.json")
// default menu item
var pages = [
  {
    /*
    component: 'VListItem',
    name: 'dashboard',
    to: '/dashboard',
    routeName: "dashboard",
    icon: 'mdi-view-dashboard',
    */
  },
]

// iterate over items and add to pages
var processRegistry = (registry) => {
    registry.map((page) => {
         if (page.display == true){
             delete page["display"]
             pages.push(page)
         }
    })
   return pages;
}

module.exports = processRegistry(registry)
// export default processRegistry(registry)
