<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <title>Portfolio</title>
        <body>
            <h1>My Portfolio</h1>

            <xsl:for-each select="portfolio/foto">
                <xsl:sort select="fecha" order="descending"/>
                <xsl:choose>
                <xsl:when test="@tecnica='Blanco y Negro'">
                    <div>
                    <xsl:attribute name="style">color: red;</xsl:attribute>
                    <h3><xsl:value-of select="titulo"/></h3>
                    <p>Técnica: <xsl:value-of select="@tecnica"/></p>
                    <img src="{url}" alt="{titulo}"/>    
                </div>
                </xsl:when>
                <xsl:otherwise>
                    <div>
                        <h3><xsl:value-of select="titulo"/></h3>
                        <p>Técnica: <xsl:value-of select="@tecnica"/></p>
                        <img src="{url}" alt="{titulo}"/>    
                    </div>
                </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>