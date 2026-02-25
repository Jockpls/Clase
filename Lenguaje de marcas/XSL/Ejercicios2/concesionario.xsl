<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
    <body>
   <table border="1">
      <tr>
         <th>Marca</th>
         <th>Modelo</th>
         <th>Año</th>
         <th>Combustible</th>
         <th>Precio</th>
      </tr>
      <xsl:for-each select="concesionario/vehiculo">
        <xsl:sort select="precio" order="descending" data-type="number"/>
         <tr>
            <xsl:choose>
                <xsl:when test="combustible='Eléctrico'">
                    <td bgcolor="lightgreen"><xsl:value-of select="marca"/></td>
                    <td bgcolor="lightgreen"><xsl:value-of select="modelo"/></td>
                    <td bgcolor="lightgreen"><xsl:value-of select="año"/></td>
                    <td bgcolor="lightgreen"><xsl:value-of select="combustible"/></td>
                    <td bgcolor="lightgreen"><xsl:value-of select="precio"/></td>
                </xsl:when>
                <xsl:otherwise>
                    <td><xsl:value-of select="marca"/></td>
                    <td><xsl:value-of select="modelo"/></td>
                    <td><xsl:value-of select="año"/></td>
                    <td><xsl:value-of select="combustible"/></td>
                    <td><xsl:value-of select="precio"/></td>
                </xsl:otherwise>
            </xsl:choose>
         </tr>
      </xsl:for-each>

    </table>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>