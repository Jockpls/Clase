<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <title>Estado del hogar inteligente</title>
        <body>
            <xsl:for-each select="hogar/dispositivo">
                    <xsl:if test="@estado='encendido' and consumo_w &lt; 100">
                        <div style="border: 1px solid green; display: inline-block; padding: 10px; margin: 5px;">
                            <p>Nombre: <xsl:value-of select="nombre"/></p>
                            <p>Ubicación: <xsl:value-of select="ubicacion"/></p>
                            <p>Consumo: <xsl:value-of select="consumo_w"/>W</p>
                        </div>
                        <br/>
                    </xsl:if>
                    <xsl:if test="@estado='encendido' and consumo_w &gt; 100">
                        <div style="border: 1px solid red; display: inline-block; padding: 10px; margin: 5px;">
                            <p>Nombre: <xsl:value-of select="nombre"/></p>
                            <p>Ubicación: <xsl:value-of select="ubicacion"/></p>
                            <p>Consumo: <xsl:value-of select="consumo_w"/>W</p>
                        </div>
                        <br/>
                    </xsl:if>
            </xsl:for-each>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>