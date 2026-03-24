<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <title>Intranet Corporativa</title>
    <body>
        <xsl:for-each select="empresa/empleado">
            <div>
                <xsl:attribute name="style">border: 2px solid red;</xsl:attribute>
                <xsl:if test="@rol='admin'">
                    <xsl:attribute name="style">background-color: gray;</xsl:attribute>
                </xsl:if>
                <p>Nombre: <xsl:value-of select="nombre"/></p>
                <p>Departamento: <xsl:value-of select="departamento"/></p>
                <p>Proyectos:</p>
                    <xsl:choose>
                        <xsl:when test="proyectos/p">
                            <ul>
                                <xsl:for-each select="proyectos/p">
                                    <li><xsl:value-of select="."/></li>
                                </xsl:for-each>
                            </ul>
                        </xsl:when>
                        <xsl:otherwise>
                            <p><i>Sin proyectos asignados</i></p>
                        </xsl:otherwise>
                    </xsl:choose>
                </div>
                <br/>
        </xsl:for-each>
    </body>
</html>    
</xsl:template>
</xsl:stylesheet>