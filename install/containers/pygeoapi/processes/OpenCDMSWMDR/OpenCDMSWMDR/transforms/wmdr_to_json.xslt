<xsl:stylesheet version="2.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:gmd="http://www.isotc211.org/2005/gmd"
    xmlns:wmdr="http://def.wmo.int/wmdr/2017"
    xmlns:om="http://www.opengis.net/om/2.0"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://def.wmo.int/wmdr/2017 http://schemas.wmo.int/wmdr/1.0RC9/wmdr.xsd">
    <xsl:output encoding="UTF-8"  omit-xml-declaration="yes"/>
    <xsl:param name="delim" select="','" />
    <xsl:param name="quote" select="'&quot;'" />
    <xsl:param name="break" select="'&#xA;'" />
    <xsl:param name="host" select="'HOST'" />
    <xsl:param name="location" select="'LOCATION'" />
    <xsl:param name="territory" select="'TERRITORY'" />
    <xsl:param name="programme" select="'PROGRAMME'" />
    <xsl:param name="observation" select="'OBSERVATION'" />
    <xsl:param name="version" select="1"/>
    <xsl:param name="user" select="'tag:beta.opencdms.org,2023:/data/user/default'"/>
    <xsl:param name="status" select="'tag:beta.opencdms.org,2023:/vocab/status/latest'"/>
    <xsl:param name="comments" select="'Record extracted from OSCAR/Surface'"/>
    <xsl:param name="time_zone" select="''"/>
    <xsl:param name="change_date" select="''"/>
    <xsl:template match="/">
        <xsl:param name="wsi" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/gml:identifier/text()"/>
        <xsl:param name="id" select="concat('tag:beta.opencdms.org,2023:',$wsi)"/>
        <xsl:param name="name" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/gml:name/text()"/>
        <xsl:param name="description" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:description/wmdr:Description/wmdr:description"/>
        <xsl:param name="facility_type" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:facilityType/@xlink:href"/>
        <xsl:param name="date_established" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:dateEstablished"/>
        <xsl:param name="date_closed" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:dateClosed"/>
        <xsl:param name="wmo_region" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:wmoRegion/@xlink:href"/>
        <xsl:param name="territory" select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:territory/wmdr:Territory/wmdr:territoryName/@xlink:href"/>
        <xsl:for-each select="/wmdr:WIGOSMetadataRecord/wmdr:facility/wmdr:ObservingFacility/wmdr:geospatialLocation">
            <xsl:variable name="pos" select="wmdr:GeospatialLocation/wmdr:geoLocation/gml:Point/gml:pos"/>
            <xsl:variable name="latitude" select="substring-before($pos,' ')"/>
            <xsl:variable name="longitude" select="substring-before(substring-after($pos,' '),' ')"/>
            <xsl:variable name="elevation" select="substring-after(substring-after($pos,' '),' ')"/>
            <xsl:variable name="valid_from" select="wmdr:GeospatialLocation/wmdr:validPeriod/gml:TimePeriod/gml:beginPosition"/>
            <xsl:variable name="valid_to" select="wmdr:GeospatialLocation/wmdr:validPeriod/gml:TimePeriod/gml:endPosition"/>
            <xsl:text>{</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>    "type": "Feature",</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>    "properties": {</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>        "wigos_station_identifier":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$wsi"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "valid_to":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$valid_to"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "facility_type_id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$facility_type"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "_version":</xsl:text><xsl:value-of select="$version"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "name":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$name"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "date_established":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$date_established"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "_change_date":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$change_date"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "description":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$description"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "date_closed":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$date_closed"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "_user_id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$user"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "wmo_region_id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$wmo_region"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "_status_id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$status"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "territory_id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$territory"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "comments":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$comments"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "elevation":</xsl:text><xsl:value-of select="$elevation"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "time_zone_id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$time_zone"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "valid_from":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$valid_from"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "links": [</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>            {"rel":"canonical", "href": "https://oscar.wmo.int/surface/#/search/station/stationReportDetails/</xsl:text><xsl:value-of select="$wsi"/><xsl:text>", "type": "text/html", "title": "Record for this station on OSCAR/Surface"}</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>        ]</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>    }</xsl:text><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>    "id":</xsl:text><xsl:value-of select="$quote"/><xsl:value-of select="$wsi"/><xsl:value-of select="$quote"/><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>    "geometry": {</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>        "type": "Point"</xsl:text><xsl:value-of select="$delim"/><xsl:value-of select="$break"/>
            <xsl:text>        "coordinates": [</xsl:text><xsl:value-of select="$longitude"/><xsl:value-of select="$delim"/><xsl:value-of select="$latitude"/><xsl:text>]</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>    }</xsl:text><xsl:value-of select="$break"/>
            <xsl:text>}</xsl:text><xsl:value-of select="$break"/>
        </xsl:for-each>
    </xsl:template>
 </xsl:stylesheet>