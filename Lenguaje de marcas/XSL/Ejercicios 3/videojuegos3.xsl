<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <title>Base de datos gaming</title>
        <body>
            <xsl:for-each select="catalogo_juegos/juego">
            <xsl:sort select="genero" order="descending"/>
            <xsl:choose>
                <xsl:when test="plataforma='PC'">
                    <div>
                        <p><xsl:value-of select="titulo"/></p>
                        <p><xsl:value-of select="plataforma"/></p>
                        <p><xsl:value-of select="genero"/></p>
                        <p><xsl:value-of select="@pegi"/></p>
                        <p>Juego disponible en Steam</p>
                    </div>
                    <br/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:choose>
                        <xsl:when test="@pegi &gt;= 18 and plataforma=PC">
                        <p><xsl:value-of select="titulo"/></p>
                        <p><xsl:value-of select="plataforma"/></p>
                        <p><xsl:value-of select="genero"/></p>
                        <p><xsl:value-of select="@pegi"/></p>
                        <p>Juego disponible en Steam</p>
                            </div>
                            <br/>
                        </xsl:when>
                        <xsl:otherwise>
                            <div>
                                <p><xsl:value-of select="titulo"/></p>
                                <p><xsl:value-of select="plataforma"/></p>
                                <p><xsl:value-of select="genero"/></p>
                                <p><xsl:value-of select="@pegi"/></p>
                            </div>
                            <br/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:otherwise>
            </xsl:choose>
            </xsl:for-each>
        </body>
    </html>

</xsl:template>
</xsl:stylesheet>