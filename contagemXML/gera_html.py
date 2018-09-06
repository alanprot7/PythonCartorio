class GeraHtml:

    def __init__(self, dic_lista, dic_valores):
        self._dic_lista = dic_lista
        self._dic_valores = dic_valores
        self._modelo = '''<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 12">
<link rel=File-List href="molde_arquivos/filelist.xml">
<style id="molde_32210_Styles">
<!--table
    {mso-displayed-decimal-separator:"\,";
    mso-displayed-thousand-separator:"\.";}
.xl1532210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:10.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial;
    mso-generic-font-family:auto;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl6532210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:10.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial;
    mso-generic-font-family:auto;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl6632210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:10.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial;
    mso-generic-font-family:auto;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl6732210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:10.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial;
    mso-generic-font-family:auto;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:1.0pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl6832210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:10.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial;
    mso-generic-font-family:auto;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:none;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl6932210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:10.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial;
    mso-generic-font-family:auto;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:none;
    border-bottom:1.0pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7032210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:left;
    vertical-align:bottom;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7132210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"Short Date";
    text-align:left;
    vertical-align:bottom;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7232210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7332210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:1.0pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7432210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:1.0pt solid windowtext;
    border-right:none;
    border-bottom:1.0pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7532210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:1.0pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:none;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7632210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:1.0pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7732210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:1.0pt solid windowtext;
    border-right:1.0pt solid windowtext;
    border-bottom:1.0pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7832210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:0;
    text-align:center;
    vertical-align:bottom;
    border-top:none;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl7932210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:none;
    border-right:none;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8032210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:none;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:none;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8132210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border-top:none;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8232210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border-top:none;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8332210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border-top:none;
    border-right:1.0pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8432210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"\#\,\#\#0";
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8532210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:none;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8632210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:none;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8732210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8832210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl8932210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:1.0pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9032210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9132210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:none;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9232210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:none;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9332210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:none;
    border-right:none;
    border-bottom:none;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9432210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:none;
    border-left:none;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9532210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:none;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9632210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"_-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;\\-\[$R$-416\]\\ * \#\,\#\#0\.00_-\;_-\[$R$-416\]\\ * \0022-\0022??_-\;_-\@_-";
    text-align:center;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:1.0pt solid windowtext;
    border-bottom:none;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9732210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:none;
    border-bottom:none;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9832210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:.5pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:1.0pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl9932210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl10032210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:General;
    text-align:general;
    vertical-align:bottom;
    border-top:.5pt solid windowtext;
    border-right:1.0pt solid windowtext;
    border-bottom:.5pt solid windowtext;
    border-left:.5pt solid windowtext;
    mso-background-source:auto;
    mso-pattern:auto;
    white-space:nowrap;}
.xl10132210
    {padding-top:1px;
    padding-right:1px;
    padding-left:1px;
    mso-ignore:padding;
    color:windowtext;
    font-size:12.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:Arial, sans-serif;
    mso-font-charset:0;
    mso-number-format:"Short Date";
    text-align:left;
    vertical-align:bottom;
    mso-background-source:auto;
    mso-pattern:auto;
    mso-protection:unlocked visible;
    white-space:nowrap;}
-->
</style>
</head>

<body>
<!--[if !excel]>&nbsp;&nbsp;<![endif]-->
<!--As seguintes informações foram geradas pelo Assistente para Publicação como
Página da Web do Microsoft Office Excel.-->
<!--Se o mesmo item for republicado a partir do Excel, todas as informações
entre as marcas DIV serão substituídas.-->
<!----------------------------->
<!--INÍCIO DA SAÍDA DO 'ASSISTENTE PARA PUBLICAÇÃO COMO PÁGINA DA WEB' DO EXCEL
-->
<!----------------------------->

<div id="molde_32210" align=center x:publishsource="Excel">

<table border=0 cellpadding=0 cellspacing=0 width=694 style='border-collapse:
 collapse;table-layout:fixed;width:521pt'>
 <col width=64 style='width:48pt'>
 <col width=139 style='mso-width-source:userset;mso-width-alt:5083;width:104pt'>
 <col width=42 style='mso-width-source:userset;mso-width-alt:1536;width:32pt'>
 <col width=149 style='mso-width-source:userset;mso-width-alt:5449;width:112pt'>
 <col width=116 style='mso-width-source:userset;mso-width-alt:4242;width:87pt'>
 <col width=120 style='mso-width-source:userset;mso-width-alt:4388;width:90pt'>
 <col width=64 style='width:48pt'>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl7032210 width=64 style='height:17.1pt;width:48pt'>DATA:</td>
  <td class=xl10132210 width=139 style='width:104pt'>COD00</td>
  <td class=xl7132210 width=42 style='width:32pt'></td>
  <td class=xl7232210 width=149 style='width:112pt'></td>
  <td class=xl7232210 width=116 style='width:87pt'></td>
  <td class=xl7232210 width=120 style='width:90pt'></td>
  <td class=xl7232210 width=64 style='width:48pt'></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl7232210 style='height:17.1pt'></td>
  <td class=xl7232210></td>
  <td class=xl7232210></td>
  <td class=xl7232210></td>
  <td class=xl7232210></td>
  <td class=xl7232210></td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl7332210 style='height:17.1pt'>QTD</td>
  <td class=xl7432210 style='border-left:none'>DESCRIÇÃO</td>
  <td class=xl7532210>&nbsp;</td>
  <td class=xl7632210 style='border-left:none'>EMOLUMENTOS</td>
  <td class=xl7632210 style='border-left:none'>FERMOJU</td>
  <td class=xl7732210 style='border-left:none'>FERC</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl7832210 style='height:17.1pt'>COD01</td>
  <td class=xl7932210 style='border-left:none'>PROTESTO</td>
  <td class=xl8032210>&nbsp;</td>
  <td class=xl8132210 style='border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD10 </td>
  <td class=xl8232210 style='border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD18 </td>
  <td class=xl8332210 style='border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD26 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl8432210 style='height:17.1pt;border-top:none'>COD02</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>APONTAMENTO</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl8732210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD11 </td>
  <td class=xl8832210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD19 </td>
  <td class=xl8932210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD27 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>COD03</td>
  <td class=xl8532210 colspan=2 style='border-right:.5pt solid black'>CANCELAMENTO</td>
  <td class=xl8732210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD12 </td>
  <td class=xl8832210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD20 </td>
  <td class=xl8932210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD28 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>COD04</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>CERTIDÃO</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl8732210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD13 </td>
  <td class=xl8832210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD21 </td>
  <td class=xl8932210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD29 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>COD05</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>INFORMAÇÃO</td>
  <td class=xl9132210 style='border-top:none'>COD09</td>
  <td class=xl8732210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD14 </td>
  <td class=xl8832210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD22 </td>
  <td class=xl8932210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD30 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>ESCRITURA</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>PROCURAÇÃO</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>AUTENTICAÇÃO</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>R. DE FIRMA</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 colspan=2 style='border-right:.5pt solid black'>C. DE
  AUTÓGRAFO</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8832210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt;border-top:none'>COD06</td>
  <td class=xl8532210 colspan=2 style='border-right:.5pt solid black'>3010 -
  DEVOLUÇÃO</td>
  <td class=xl8832210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD15 </td>
  <td class=xl8832210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD23 </td>
  <td class=xl8932210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD31 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9232210 style='height:17.1pt;border-top:none'>COD07</td>
  <td class=xl9332210 style='border-left:none'>3021 - SUSTADOS</td>
  <td class=xl9432210 style='border-top:none'>&nbsp;</td>
  <td class=xl9532210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD16 </td>
  <td class=xl9532210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD24 </td>
  <td class=xl9632210 style='border-top:none;border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD32 </td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9032210 style='height:17.1pt'>COD08</td>
  <td class=xl9732210 style='border-left:none'>EDITAL</td>
  <td class=xl8632210>&nbsp;</td>
  <td class=xl8832210 style='border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD17 </td>
  <td class=xl8832210 style='border-left:none'><span
  style='mso-spacerun:yes'> </span>R$COD25 </td>
  <td class=xl8932210 style='border-left:none'><span
  style='mso-spacerun:yes'> </span>R$<span
  style='mso-spacerun:yes'>                  </span>-<span
  style='mso-spacerun:yes'>   </span></td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9832210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-left:none'>&nbsp;</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl9932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl9932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl10032210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9832210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl9932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl9932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl10032210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl9832210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl8532210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl8632210 style='border-top:none'>&nbsp;</td>
  <td class=xl9932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl9932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl10032210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl7232210></td>
 </tr>
 <tr height=22 style='mso-height-source:userset;height:17.1pt'>
  <td height=22 class=xl6532210 style='height:17.1pt;border-top:none'>&nbsp;</td>
  <td class=xl6932210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl6832210 style='border-top:none'>&nbsp;</td>
  <td class=xl6632210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl6632210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl6732210 style='border-top:none;border-left:none'>&nbsp;</td>
  <td class=xl1532210></td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=64 style='width:48pt'></td>
  <td width=139 style='width:104pt'></td>
  <td width=42 style='width:32pt'></td>
  <td width=149 style='width:112pt'></td>
  <td width=116 style='width:87pt'></td>
  <td width=120 style='width:90pt'></td>
  <td width=64 style='width:48pt'></td>
 </tr>
 <![endif]>
</table>

</div>


<!----------------------------->
<!--FIM DA SAÍDA DO 'ASSISTENTE PARA PUBLICAÇÃO COMO PÁGINA DA WEB' DO EXCEL-->
<!----------------------------->
</body>

</html>
'''

    def geraHtml(self):
        caminho = ""
        nome_arquivo = self._dic_lista["data"].replace("/","")
        _saida = open(caminho + nome_arquivo + ".html", "w")
        modelo_final = self._modelo
        modelo_final = modelo_final.replace("COD00" , self._dic_lista["data"])
        modelo_final = modelo_final.replace("COD01" , str(self.somaProtesto()[3]))
        modelo_final = modelo_final.replace("COD02" , str(self.somaApontamento()[3]))
        modelo_final = modelo_final.replace("COD03" , str(self._dic_lista["003007"]))
        modelo_final = modelo_final.replace("COD04" , str(self._dic_lista["003008"]))
        modelo_final = modelo_final.replace("COD05" , str(self._dic_lista["003009"] + self._dic_lista["003020"]))
        modelo_final = modelo_final.replace("COD06" , str(self._dic_lista["003010"]))
        modelo_final = modelo_final.replace("COD07" , str(self._dic_lista["003021"]))
        modelo_final = modelo_final.replace("COD08" , str(self._dic_lista["003019"]))
        modelo_final = modelo_final.replace("COD09" , str(self._dic_lista["adicionalPositiva"]))
        valor = self.criaEspacoHtml("%.2f" % (self.somaProtesto()[0]))
        modelo_final = modelo_final.replace("COD10" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self.somaApontamento()[0]))
        modelo_final = modelo_final.replace("COD11" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003007"][0]))
        modelo_final = modelo_final.replace("COD12" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003008"][0]))
        modelo_final = modelo_final.replace("COD13" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003009"][0] + self._dic_valores["003020"][0]))
        modelo_final = modelo_final.replace("COD14" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003010"][0]))
        modelo_final = modelo_final.replace("COD15" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003021"][0]))
        modelo_final = modelo_final.replace("COD16" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003019"][0]))
        modelo_final = modelo_final.replace("COD17" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self.somaProtesto()[1]))        
        modelo_final = modelo_final.replace("COD18" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self.somaApontamento()[1]))        
        modelo_final = modelo_final.replace("COD19" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003007"][1]))
        modelo_final = modelo_final.replace("COD20" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003008"][1]))
        modelo_final = modelo_final.replace("COD21" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003009"][1] + self._dic_valores["003020"][1]))
        modelo_final = modelo_final.replace("COD22" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003010"][1]))
        modelo_final = modelo_final.replace("COD23" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003021"][1]))
        modelo_final = modelo_final.replace("COD24" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003019"][1]))
        modelo_final = modelo_final.replace("COD25" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self.somaProtesto()[2]))          
        modelo_final = modelo_final.replace("COD26" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self.somaApontamento()[2]))        
        modelo_final = modelo_final.replace("COD27" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003007"][2]))
        modelo_final = modelo_final.replace("COD28" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003008"][2]))
        modelo_final = modelo_final.replace("COD29" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003009"][2] + self._dic_valores["003020"][2]))
        modelo_final = modelo_final.replace("COD30" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003010"][2]))
        modelo_final = modelo_final.replace("COD31" , valor)
        valor = self.criaEspacoHtml("%.2f" % (self._dic_valores["003021"][2]))
        modelo_final = modelo_final.replace("COD32" , valor)
        _saida.write(modelo_final)
        _saida.close()

    def criaEspacoHtml(self, valor):
        tamanho = 13
        tamanho = tamanho - len(valor)
        caractere_espaco = ""
        for i in range(0,tamanho):
            caractere_espaco += "&nbsp;"

        return caractere_espaco + str(valor)

    def somaApontamento(self):
        emolumento = 0.0
        fermoju = 0.0
        selo = 0.0
        qtd_atos = 0

        for key in self._dic_valores:
            if key == "003001":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]
            if key == "003002":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003003":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003004":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003005":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003006":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003017":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003018":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "006012":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "001006":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "005023":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                

        return [emolumento, fermoju, selo, qtd_atos]


    def somaProtesto(self):
        emolumento = 0.0
        fermoju = 0.0
        selo = 0.0
        qtd_atos = 0

        for key in self._dic_valores:
            if key == "003011":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]
            if key == "003012":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003013":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003014":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003015":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                
            if key == "003016":
                emolumento += self._dic_valores[key][0]
                fermoju += self._dic_valores[key][1]
                selo += self._dic_valores[key][2]
                qtd_atos += self._dic_lista[key]                

        return [emolumento, fermoju, selo, qtd_atos]
