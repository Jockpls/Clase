<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <body>
            <h1>Entrantes</h1>
            <table border="1">
                <tr>
                    <th>Nombre del Plato</th>
                    <th>Precio</th>
                    <th>Descripción</th>
                </tr>
                <xsl:for-each select="menu/plato[@categoria='Entrantes']">
                    <tr>
                        <td><xsl:value-of select="nombre_plato"/></td>
                        <td><xsl:value-of select="precio_unitario"/></td>
                        <td><xsl:value-of select="descripcion"/></td>
                    </tr>
                </xsl:for-each>
            </table>
            <h2>Platos Principales</h2>
            <table border="1">
                <tr>
                    <th>Nombre del Plato</th>
                    <th>Precio</th>
                    <th>Descripción</th>
                </tr>
                <xsl:for-each select="menu/plato[@categoria='Platos Principales']">
                    <tr>
                        <td><xsl:value-of select="nombre_plato"/></td>
                        <xsl:choose>
                            <xsl:when test="precio_unitario &gt; 15">
                                <td style="font-weight: bold;"><xsl:value-of select="precio_unitario"/></td>
                            </xsl:when>
                            <xsl:otherwise>
                                <td><xsl:value-of select="precio_unitario"/></td>
                            </xsl:otherwise>
                        </xsl:choose>
                        <td><xsl:value-of select="descripcion"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>