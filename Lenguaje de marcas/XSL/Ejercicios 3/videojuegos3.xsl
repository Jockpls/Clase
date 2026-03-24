<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <head>
            <title>Base de Datos de Gaming</title>
        </head>
        <body>
            <xsl:for-each select="catalogo_juegos/juego">
                <xsl:sort select="genero" order="ascending"/>

                <div>
                    <xsl:if test="@pegi &gt; '17'">
                        <xsl:attribute name="style">background-color: red;</xsl:attribute>
                    </xsl:if>

                    <p>Título: <xsl:value-of select="titulo"/></p>
                    <p>Plataforma: <xsl:value-of select="plataforma"/></p>
                    <p>Género: <xsl:value-of select="genero"/></p>
                    <p>PEGI: <xsl:value-of select="@pegi"/></p>

                    <xsl:if test="plataforma = 'PC'">
                        <p>Disponible en Steam</p>
                    </xsl:if>

                    <xsl:if test="@pegi &gt; '17'">
                        <p>Aviso: Contenido Adulto</p>
                    </xsl:if>
                </div>
                <hr/> </xsl:for-each>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>