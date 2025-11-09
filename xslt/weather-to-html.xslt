<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes"/>


<xsl:template match="/weatherReport">
<html>
<head>
<title>Weather report</title>
</head>
<body>
<h2>Weather report for <xsl:value-of select="city"/></h2>
<table border="1">
<tr><th>Date</th><td><xsl:value-of select="date"/></td></tr>
<tr><th>Temperature</th><td><xsl:value-of select="temperature"/> (<xsl:value-of select="temperature/@unit"/>)</td></tr>
<tr><th>Humidity</th><td><xsl:value-of select="humidity"/> (<xsl:value-of select="humidity/@unit"/>)</td></tr>
<tr><th>Wind</th><td><xsl:value-of select="windSpeed"/> (<xsl:value-of select="windSpeed/@unit"/>)</td></tr>
<tr><th>Condition</th><td><xsl:value-of select="condition"/></td></tr>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>