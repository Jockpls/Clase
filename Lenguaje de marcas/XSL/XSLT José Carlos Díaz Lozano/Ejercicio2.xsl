<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
    <body>
        <table border='1'>
            <tr>
                <th>Nombre completo</th>
                <th>Diagnóstico</th>
                <th>Médico asignado</th>
            </tr>
            <xsl:for-each select="hospital/paciente">
            <xsl:sort select="fecha_ingreso" order="ascending"/>
                <tr>
                    <td><xsl:value-of select="nombre_completo"/></td>
                    <td><xsl:value-of select="diagnostico"/></td>
                    <td><xsl:value-of select="medico_asignado"/></td>
                </tr>
            </xsl:for-each>
        </table>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>