<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <body>
           <table border='1'>
                <tr>
                    <th>Emisor</th>
                    <th>CIF</th>
                    <th>Dirección</th>
                </tr>
                <xsl:for-each select="envios/albaran">
                <xsl:sort select="emisor/largo"/>
                <tr>
                    <td><xsl:value-of select="emisor/nombre"/></td>
                    <td><xsl:value-of select="emisor/cif"/></td>
                    <td><xsl:value-of select="emisor/direccion"/></td>
                </tr>
                </xsl:for-each>
           </table>
        <br/>
           <table border="1">
            <tr>
                <th>Nombre</th>
                <th>DNI</th>
                <th>Dirección</th>
            </tr>
            <xsl:for-each select="envios/albaran">
            <xsl:sort select="receptor/nombre" order="descending"/>
            <tr>
                <td><xsl:value-of select="receptor/nombre"/></td>
                <td><xsl:value-of select="receptor/dni"/></td>
                <td><xsl:value-of select="receptor/direccion_entrega"/></td>
            </tr>
            </xsl:for-each>
           </table>
           <br/>

            <table border="1">
                <tr>
                    <th>Tipo de Contenido</th>
                    <th>Largo</th>
                    <th>Ancho</th>
                    <th>Alto</th>
                </tr>
                <xsl:for-each select="envios/albaran">
                    <xsl:if test="detalle_paquete/dimensiones/largo > 20 and 
                                  detalle_paquete/dimensiones/ancho > 15 and 
                                  detalle_paquete/dimensiones/alto > 10">
                        <tr>
                            <td><xsl:value-of select="detalle_paquete/tipo_contenido"/></td>
                            <td><xsl:value-of select="detalle_paquete/dimensiones/largo"/></td>
                            <td><xsl:value-of select="detalle_paquete/dimensiones/ancho"/></td>
                            <td><xsl:value-of select="detalle_paquete/dimensiones/alto"/></td>
                        </tr>
                    </xsl:if>
                </xsl:for-each>
            </table> 
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>
