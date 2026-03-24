<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <head>
            <title>Viajes</title>
        </head>
        <body>
            <xsl:for-each select="muro_viajes/post">
                <div>
                    <h2>Usuario: <xsl:value-of select="usuario"/></h2>
                    <p>Comentario: <xsl:value-of select="comentario"/></p>
                    <xsl:if test="puntuacion='5'">
                        <p>Puntuación: <br/><img src="3estrellas.jpeg" width="250px" height="auto"></img></p>
                    </xsl:if>
                    <xsl:if test="puntuacion='4'">
                        <p><img src="4estrellas.png" width="250px" height="auto"></img></p>
                    </xsl:if>
                    <xsl:if test="puntuacion='3'">
                        <p><img src="5estrellas.jpg" width="250px" height="auto"></img></p>
                    </xsl:if>
                </div>
            </xsl:for-each>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>