<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <body>
        <table border="1">
            <tr>
                <th>Nombre de la Banda</th>
                <th>Género</th>
                <th>escenario</th>
                <th>Hora de Inicio</th>
            </tr>
        <xsl:for-each select="festival/banda">
        <xsl:sort select="hora_inicio" order="ascending"/>
                <tr>
                    <td><xsl:value-of select="nombre_banda"/></td>
                    <td><xsl:value-of select="genero"/></td>
                    <td><xsl:value-of select="escenario"/></td>
                    <td><xsl:value-of select="hora_inicio"/></td>
                </tr>
            </xsl:for-each>
        </table>
        <div style="border: 2px solid black; display: inline-block; margin-top: 20px; padding: 10px;">
            <h2>Artistas Principales</h2>
            <xsl:for-each select="festival/banda[@tipo='especial']">
            <ul>    
                <li><xsl:value-of select="nombre_banda"/></li>
            </ul>
            </xsl:for-each>
        </div>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>