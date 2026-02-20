<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
    <body>
        <table border="1">
        <tr>
            <th>Título_curso</th>
            <th>Profesor</th>
            <th>Descripción</th>
            <th>Video</th>
        </tr>
        <xsl:for-each select="academia/curso">
        <xsl:sort select="titulo_curso"/>
        <tr>
            <td><xsl:value-of select="titulo_curso"/></td>
            <td><xsl:value-of select="profesor"/></td>
            <td><xsl:value-of select="descripcion"/></td>
            <td>
                <table>
                <xsl:for-each select='temario/modulo/video'>
                    <tr>
                        <td>
                            <xsl:value-of select="."/>
                        </td>
                    </tr>
                </xsl:for-each>
                </table>
            </td>
        </tr>
        </xsl:for-each>
        </table>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>