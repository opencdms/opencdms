'use strict'

import navs from "./_nav.mjs"
import fs from 'fs'
import path from 'path';
import {fileURLToPath} from 'url';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const __node_modules_path = path.resolve(__dirname, "..", "node_modules")


function isPackageInstalled(packageName) {
    let pkgPath = `${__node_modules_path}/${packageName}/package.json`
    try {
        fs.accessSync(pkgPath, fs.constants.R_OK)
        return true;

    } catch (error) {
        return false;
    }

}

function generatePages(navs) {


        navs.map( (nav) =>  {
            if (nav.to !== undefined && nav.routeName !== "Dashboard" ) {
                // Page is the name of the opencdms commponent
                console.log(nav)
                let parts = nav.package.split("/")
                if (parts[0] !== "@opencdms"){
                     console.log(`Package name must be prefixed by @opencdms but got ${parts[0]}`)
                     return
                }
                let page = parts[1]
                let opencdmsPackageName = nav.package
                if (isPackageInstalled(opencdmsPackageName) === false){
                    console.error(`Install the package ${opencdmsPackageName} by running npm install --save ${opencdmsPackageName}`)
                    return
                }
                // Route name is the unique vuejs route name of the page
                let name = nav.routeName

var template = `
<template lang="">
    <opencdms-${page}></opencdms-${page}>
</template>
<script>
import "@opencdms/${page}"
export default {
    name: "${name}"
}
</script>
<style lang="">

</style>

`               // The view filename is generated from the route name
                let viewFile = `${__dirname}/views/${name}.vue`
                fs.open(viewFile, 'wx', (err, fd) => {
                    if (err) {
                      if (err.code === 'EEXIST') {
                        console.error(`${viewFile} already exists`);
                        return;
                      }

                      throw err;
                    }

                    try {
                        var writeStream = fs.createWriteStream(`${__dirname}/views/${name}.vue`);
                        writeStream.write(template);
                        writeStream.end();
                    } finally {
                      fs.close(fd, (err) => {
                        if (err) throw err;
                      });
                    }
                  });
            }
        })
    }



generatePages(navs)
