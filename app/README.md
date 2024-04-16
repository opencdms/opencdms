# OpenCDMS app 

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```


## App Configuration

This application can be configured to selectively display pages declared in the route list. By default, only the Dashboard link will appear on the sidebar navigation menu. To add more links in the sidebar menu:

1.  All the routes would be declared as the src/routes/routes.js as in a normal vuejs application.
2.  Go to  `src/registry.json` file. Each entry in the registry represents a navigation link. 
3.  Set the display property to the desired value (true or false). Only the links with display set to true would be visible in the navigation bar and the  final build routes.

This implies that the registry entries set to false would not be available in the application.


eg
```
// src/registry.json
[
    {
        "component": "CNavItem", // Name of the render component
        "name": "Hidden",  // The name of the element visible to the user on the side navigation bar
        "to": "/hidden", // Path must correspond to the route path declared in src/routes/route.js 
        "icon": "cil-drop", // Display icon
        "display": false // will not be displayed and user will not be able to see this page
        "routeName": "Hidden", // The vuejs routename for this entry
        "package": "@opencdms/hidden" // The npm package name of the webcomponent to be rendered in this page
      },
       {
        "component": "CNavItem", // Name of the render component
        "name": "Test Page",  // The name of the element visible to the user 
        "to": "/test-page", // Path must correspond to the route path declared in src/routes/route.js 
        "icon": "cil-drop", // Display icon
        "display": true // will be displayed
        "routeName": "Test", // The vuejs routename for this entry
        "package": "@opencdms/helloworld" // The npm package name of the webcomponent to be rendered in this page
      }
]
```

### Web Components

We can render web components built using any javascript framework in this application shell.

To render a web component:

1. Create the web component and publish in npm or define it in the `src/web-components` folder.

2. Ensure that the tagname of the web component is prefixed with `opencdms-` eg `<opencdms-helloworld>....</opencdms-helloworld>`.

3. Install the webcomponent by running npm install --save @opencdms/webcomponentName.

4. Create a registry entry in src/registry.json for the page created above. Set the display to true or false as you desire.

5. Generate the view files by running `npm run views:generate`
The generated view filenames in src/views folder corresponds to the routeName property in the registry.json file hence routeName property must be unique. You can customise the generated view files as you want. Running the views:generate command does not overwrite existing files.

6. Launch the application. npm run serve 
