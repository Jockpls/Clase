<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <body>
            <table border="1">
                <tr>
                    <th>Titular Principal</th>
                    <th>Titular del Artículo</th>
                    <th>Autor del Artículo</th>
                </tr>
                <xsl:for-each select="hemeroteca/ejemplar">
                    <xsl:sort select="ejemplar/@fecha_publicacion" order="descending"/>
                        <tr>
                            <td><xsl:value-of select="portada/titular_principal"/></td>
                            <td><xsl:value-of select="seccion/articulo/titular"/></td>
                            <td><xsl:value-of select="seccion/articulo/autor"/></td>
                        </tr>
                </xsl:for-each>
            </table>
            <br/>
            <table border="1">
                <tr>
                    <th>Titular del Artículo</th>
                    <th>Autor del Artículo</th>
                </tr>
                <xsl:for-each select="hemeroteca/ejemplar/seccion[@nombre='Cultura']/articulo">
                    <xsl:sort select="@fecha_publicacion" order="descending"/>
                <tr>
                        <td><xsl:value-of select="titular"/></td>
                        <td><xsl:value-of select="autor"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>