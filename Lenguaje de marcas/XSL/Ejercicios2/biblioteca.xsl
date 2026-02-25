<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
    <html>
        <body>
        <table border='1'>
            <tr>
                <th>ISBN</th>
                <th>Título</th>
                <th>Autor</th>
                <th>Editorial</th>
            </tr>
            <xsl:for-each select="biblioteca/libro">
            <xsl:if test="año_publicacion &gt; 2020">
                <tr>
                    <td><xsl:value-of select="@isbn"/></td>
                    <td><xsl:value-of select="titulo_libro"/></td>
                    <td><xsl:value-of select="autor"/></td>
                    <td><xsl:value-of select="editorial"/></td>
                </tr>
            </xsl:if>
        </xsl:for-each>
        </table>
        <ul>
            <xsl:for-each select="biblioteca/libro">
            <xsl:sort select="autor"/>
            <li><xsl:value-of select="autor"/></li>
            </xsl:for-each>
        </ul>
        </body>
    </html>
    </xsl:template>
</xsl:stylesheet>