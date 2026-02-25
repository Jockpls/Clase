<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
    <body>
        <table border="1">
            <tr>
                <th>Codigo de Producto</th>
                <th>Nombre del Producto</th>
                <th>Stock</th>
                <th>Proveedor</th>
            </tr>
            <xsl:for-each select="almacen/producto">
            <xsl:sort select="proveedor" order="ascending"/>
            <tr>
            <xsl:attribute name="bgcolor">    
            <xsl:choose>
            <xsl:when test="stock_actual &lt; 11">red</xsl:when>
            <xsl:when test="stock_actual &lt; 21 and stock_actual &gt;= 11">yellow</xsl:when>
            <xsl:otherwise>green</xsl:otherwise>
            </xsl:choose>
            </xsl:attribute>
                    <td><xsl:value-of select="codigo_producto"/></td>
                    <td><xsl:value-of select="nombre"/></td>
                    <td><xsl:value-of select="stock_actual"/></td>
                    <td><xsl:value-of select="proveedor"/></td>
            </tr>
            </xsl:for-each>
        </table>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>